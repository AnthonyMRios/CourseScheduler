###############################################################################
# main.py
# Anthony Rios
# Description:
#   This file contains the genetic algorithm that will create a schedule that
#   follows a set of constraints.
###############################################################################
import random

###############################################################################
# genAlg(numCourses,courses,popSize,times,rooms,maxIters,isElite)
# Description:
#   This function will take a set of courses with specifyed constraints and
#   schedule them.
#
# Input Parameters:
#   numCourses - This should be an int that represents the # of courses to be
#                scheduled.
#   courses - This should be a list that contains represents all the courses
#             and constraints that the algorithm will need to be scheduled.
#   popSize - This should be an int that represents the # of chromosomes you
#             want in your population.
#   times - This should be a list of all the possible times available for courses.
#   rooms -  This should be a list of all the possible rooms avail. for courses.
#   maxIters - This should be the maximum times to go through the main genetic
#              algorithm loop.
#   isElite - This is a boolean value which allows either tournament style
#             selection or elitism.
#
# Returns:
#   The function will return a list that contains the original course constraints
#   and the room and time allocated for that course.
###############################################################################
def genAlg(numCourses,courses,popSize,times,rooms,maxIters,isElite):
	population = []
	fit = []
	for i in range(0,popSize):
		for j in range(0,numCourses):
			population.append(times[random.randrange(0,len(times))])
			population.append(rooms[random.randrange(0,len(rooms))])
			#Course
			population.append(courses[0+5*j])
			#Professor
			population.append(courses[1+5*j])
			#Requested Times
			population.append(courses[2+5*j])
			#Requested Rooms
			population.append(courses[3+5*j])
			#Size
			population.append(courses[4+5*j])

	fit = fitness(population,popSize,numCourses,rooms,times)

	i = 0
	while (i < maxIters) and ((float(max(fit))/(numCourses*7)) < 0.9):
		print i
		newPop = []
		toPull = fit[:]
		toPull.sort()
		toPull = toPull[(len(toPull)-int(0.1*len(toPull))):len(toPull)]
		topIndexs = []
		tempFit = fit[:]
		tempPop = []
		for j in range(0,len(toPull)):
			topIndexs.append(tempFit.index(toPull[j]))
			tempFit[topIndexs[j]] = 0
			tempPop += population[topIndexs[j]*7*numCourses:(topIndexs[j]*7*numCourses)+7*numCourses]

		for j in range(0,popSize):
			if isElite:
				howToReproduce = random.random()
				r = random.randrange(0,len(topIndexs))
				winner = tempPop[(r*numCourses*7):((r*numCourses*7)+(numCourses*7))]
				child = 0

				if howToReproduce < 0.15:
					child = mutate(winner,numCourses,times,rooms)
				else:
					howToReproduce = random.randrange(0,3)
					if howToReproduce == 0:
						child = swapRooms(winner,numCourses,rooms)
					elif howToReproduce == 1:
						child = swapTimes(winner,numCourses,times)
					else:
						child = changeCourseTime(winner,numCourses,times)

				if fitness(child,1,numCourses,rooms,times)[0] > fitness(winner,1,numCourses,rooms,times)[0]:
					newPop += child
				else:
					newPop += winner
			else:
				pick1 = random.randrange(0,popSize)
				pick2 = random.randrange(0,popSize)

				winner = 0
				if fit[pick1] > fit[pick2]:
					winner = pick1
				else:
					winner = pick2

				winner = population[(winner*numCourses*7):((winner*numCourses*7)+(numCourses*7))]

				howToReproduce = random.random()
				child = 0

				if howToReproduce < 0.15:
					child = mutate(winner,numCourses,times,rooms)
				else:
					howToReproduce = random.randrange(0,3)
					if howToReproduce == 0:
						child = swapRooms(winner,numCourses,rooms)
					elif howToReproduce == 1:
						child = swapTimes(winner,numCourses,times)
					else:
						child = changeCourseTime(winner,numCourses,times)

				if fitness(child,1,numCourses,rooms,times)[0] > fitness(winner,1,numCourses,rooms,times)[0]:
					newPop += child
				else:
					newPop += winner

		population = newPop[:]
		fit = fitness(population,popSize,numCourses,rooms,times)
		#sfit = fit[:]
		#sfit.sort()
		#file = open("maxs.txt",'a')
		#file.write(str(float(max(fit))/(numCourses*5))+'\n')
		#file.close
		#file = open("pop.txt",'a')
		#file.write(str(float(sum(fit))/(popSize*numCourses*5))+'\n')
		#file.close
		#print "Fitness: " + str(sum(fit)/(popSize*numCourses*5))
		i += 1

	maxIndex = fit.index(max(fit))
	return population[7*maxIndex:7*maxIndex+7*numCourses]

###############################################################################
# swapRooms(schedule,numCourses,rooms)
# Description:
#   This method randomly picks two rooms and swaps the courses in those rooms.
#
# Input Parameters:
#   schedule - This single a single chromosome (schedule).
#   numCourses - This is the number of courses in the schedule.
#   rooms - This is the possible rooms available for courses.
#
# Returns:
#   Returns a new schedule.
###############################################################################
def swapRooms(schedule,numCourses,rooms):
  sched = schedule[:]
  room1 = rooms[random.randrange(0,len(rooms))]
  room2 = rooms[random.randrange(0,len(rooms))]
  for i in range(0,len(sched),7):
    if sched[i+1] == room1:
      sched[i+1] = room2
    elif sched[i+1] == room2:
      sched[i+1] = room1

  return sched

###############################################################################
# swapTimes(schedule,numCourses,times)
# Description:
#   This method randomly picks two times and swaps the courses in those times.
#
# Input Parameters:
#   schedule - This single a single chromosome (schedule).
#   numCourses - This is the number of courses in the schedule.
#   times - This is the possible rooms times for courses.
#
# Returns:
#   Returns a new schedule.
###############################################################################
def swapTimes(schedule,numCourses,times):
  sched = schedule[:]
  time1 = times[random.randrange(0,len(times))]
  time2 = times[random.randrange(0,len(times))]
  for i in range(0,len(sched),7):
    if sched[i] == time1:
      sched[i] = time2 
    elif sched[i] == time2:
      sched[i] = time1 

  return sched

###############################################################################
# changeCourseTime(schedule,numCourses,times)
# Description:
#   This method randomly changes a time of a single course.
#
# Input Parameters:
#   schedule - This single a single chromosome (schedule).
#   numCourses - This is the number of courses in the schedule.
#   times - This is the possible rooms times for courses.
#
# Returns:
#   Returns a new schedule.
###############################################################################
def changeCourseTime(schedule,numCourses,times):
  sched = schedule[:]
  time = times[random.randrange(0,len(times))]
  course= random.randrange(0,numCourses)

  sched[course*7] = time

  return sched

###############################################################################
# mutate(schedule,numCourses,times,rooms)
# Description:
#   This method randomly changes a time and rooms of a single course.
#
# Input Parameters:
#   schedule - This single a single chromosome (schedule).
#   numCourses - This is the number of courses in the schedule.
#   times - This is the possible rooms times for courses.
#   rooms - This is the possible rooms rooms for courses.
#
# Returns:
#   Returns a new schedule.
###############################################################################
def mutate(schedule,numCourses,times,rooms):
  sched = schedule[:]
  time = times[random.randrange(0,len(times))]
  room = rooms[random.randrange(0,len(rooms))]
  course= random.randrange(0,numCourses)

  sched[course*7] = time
  sched[course*7+1] = room 

  return sched

###############################################################################
# fitness(pop,popSize,numCourses,rooms,times)
# Description:
#
# Input Parameters:
#   popSize - Number of schedules being passed to the function.
#   numCourses - Number of courses in each schedule.
#   rooms - Possible rooms for a schedule.
#   times - Possible times for a schedule.
#
# Returns:
###############################################################################
def fitness(pop,popSize,numCourses,rooms,times):

	fit = []

	for i in range(0,popSize):
		afit = 0
		curChrom = i*numCourses*7
		for j in range(0,numCourses*7,7):
			sameTimeSameRoom = 2
			sameTimeSameProf = 2
			requestedRoom = 0
			requestedTime = 0
			roomSizeNeed = 1
			tempTime = pop[curChrom+j]
			tempRoom = pop[curChrom+j+1]
			tempProf = pop[curChrom+j+3]
			
			for k in range(0,len(pop[curChrom+j+5])):
				if(pop[curChrom+j+5][k] == tempRoom):
					requestedRoom = 1
					break
			#if(tempTime != pop[curChrom+j+4]):
			#	requestedTime = 0
			for k in range(0,len(pop[curChrom+j+4])):
				if(pop[curChrom+j+4][k] == tempTime):
					requestedTime = 1
					break
			#if(tempRoom != pop[curChrom+j+5]):
			#	requestedRoom = 0pop[curChrom+j+5]vc

			for k in range(j+7,numCourses*7,7):
				if (tempTime == pop[curChrom+k]) and (tempRoom == pop[curChrom+k+1]):
					sameTimeSameRoom = 0
				if (tempTime == pop[curChrom+k]) and (tempProf == pop[curChrom+k+3]):
					sameTimeSameProf = 0

			afit += sameTimeSameRoom + sameTimeSameProf + requestedRoom + requestedTime + roomSizeNeed     
		fit.append(afit)
	return fit

	
# JUST FOR TESTING
def test():
	courses = ['CSC115','CSC215','CSC350','CSC450']
	profs = ['Crawley','Thorne','Leverenz','White','Desario','Dickenson','Rosenstad','Harris']
	times = ['MWF8-9','MWF9-10','MWF10-11','MWF1-2','MWF2-3','TTH930-1045','TTH1245-2','TTH210-325']
	rooms = ['ASC332','ASC333','ASC331','ASC330','ASCLAB']

	initial = []

	for i in range(0,25):
		initial.append(courses[random.randrange(0,4)])
		initial.append(profs[random.randrange(0,8)])
		temp = []
		temp.append(times[random.randrange(0,8)])
		temp.append(times[random.randrange(0,8)])
		initial.append(temp)
		#initial.append(times[random.randrange(0,8)])
		temp2 = []
		temp2.append(rooms[random.randrange(0,5)])
		temp2.append(rooms[random.randrange(0,5)])
		initial.append(temp2)
		#initial.append(rooms[random.randrange(0,5)])
		initial.append(20)

	printCourse(genAlg(25,initial,100,times,rooms,1000,True))

	return

# JUST FOR TESTING
def printCourse(course):
  print course
  for i in range(0,len(course),7):
    print "Time: " + course[i]
    print "Room: " + course[i+1]
    print "Course: " + course[i+2]
    print "Professor: " + course[i+3]
    print "Requested Time: " + course[i+4]
    print "Requested Room: " + course[i+5]
    print "Needed Room Size:" + str(course[i+6])

# JUST FOR TESTING
def temp():
	courses = ['CSC115','CSC215','CSC350','CSC450']
	profs = ['Crawley','Thorne','Leverenz','White','Desario','Dickenson','Rosenstad','Harris']
	times = ['MWF8-9','MWF9-10','MWF10-11','MWF1-2','MWF2-3','TTH930-1045','TTH1245-2','TTH210-325']
	rooms = ['ASC332','ASC333','ASC331','ASC330','ASCLAB']

	initial = []
	file = open("C:\\Users\\User\\Documents\\consts.txt",'w')

	for i in range(0,25):
		file.write(profs[random.randrange(0,8)]+"\n")
		file.write(courses[random.randrange(0,4)]+"\n")
		file.write(rooms[random.randrange(0,5)]+"\n")	
		file.write(str(20)+"\n")		
		file.write(times[random.randrange(0,8)]+"\n")

	file.close()
