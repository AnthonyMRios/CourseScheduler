###############################################################################
# project2.py
# Anthony Rios
# Description:
# This file contains the GUI code that is used to insert constraints and
# other informatin to create a schedule around.
###############################################################################
import wx
import os
import sys
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
import wx.lib.mixins.listctrl  as  listmix
import main

###############################################################################
# InsertRoomDia(wx.Dialog)
# Description:
#   This class is used to create the Insert Room Dialog.
###############################################################################
class InsertRoomDia(wx.Dialog):
	###########################################################################
	# __init__(self,parent,id,title)
	# Description:
	#   Constructor for the InsertRoomClass.
	# Input Parameters:
	#   title - title for the dialog window.
	###########################################################################
	def __init__(self,parent,id,title):
		self.tp = parent
		wx.Dialog.__init__(self,parent,id,title)
		self.panel = wx.Panel(self,-1)
		hbox = wx.BoxSizer(wx.VERTICAL)
		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.blab = wx.StaticText(self,label="Building ID: ")
		self.bid = wx.TextCtrl(self)
		vbox1.Add(self.blab,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox1.Add(self.bid,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox1,proportion=0,flag=wx.ALL,border=5)
		vbox2 = wx.BoxSizer(wx.HORIZONTAL)
		self.rlab = wx.StaticText(self,label="    Room #: ")
		self.rnum = wx.TextCtrl(self)
		vbox2.Add(self.rlab,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox2.Add(self.rnum,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox2,proportion=0,flag=wx.ALL,border=5)
		vbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.rsize = wx.StaticText(self,label=" Class Size: ")
		self.csize = wx.TextCtrl(self)
		vbox3.Add(self.rsize,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox3.Add(self.csize,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox3,proportion=0,flag=wx.ALL,border=5)
		self.submit = wx.Button(self,-1,'Submit')
		hbox.Add(self.submit,proportion=0,flag=wx.ALIGN_CENTER,border=5)
		
		self.Bind(wx.EVT_BUTTON,self.insRoom,self.submit)
		
		self.SetSizer(hbox)
		hbox.Fit(self)	
		
	###########################################################################
	# insRoom(self,e)
	# Description:
	#   This method takes the data the user input and inserts it into the room
	#   listctrl widget.
	###########################################################################
	def insRoom(self,e):
		self.tp.roomPage.insertRoom(self.bid.GetValue() + self.rnum.GetValue(),self.csize.GetValue())
		self.Close(True)

class InsertConstraintDia(wx.Dialog):
	###########################################################################
	# __init__(self,parent,id,title)
	# Description:
	#   Constructor for the InsertRoomClass.
	# Input Parameters:
	#   title - title for the dialog window.
	###########################################################################
	def __init__(self,parent,id,title):
		self.tp = parent
		wx.Dialog.__init__(self,parent,id,title)
		self.panel = wx.Panel(self,-1)
		hbox = wx.BoxSizer(wx.VERTICAL)
		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.snameid = wx.StaticText(self,label="           Professor: ")
		self.sname = wx.TextCtrl(self)
		vbox1.Add(self.snameid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox1.Add(self.sname,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox1,proportion=0,flag=wx.ALL,border=5)
		vbox2 = wx.BoxSizer(wx.HORIZONTAL)
		self.courseId = wx.StaticText(self,label="               Course: ")
		self.course = wx.TextCtrl(self)
		vbox2.Add(self.courseId,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox2.Add(self.course,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox2,proportion=0,flag=wx.ALL,border=5)
		vbox4 = wx.BoxSizer(wx.HORIZONTAL)
		self.rroomid = wx.StaticText(self,label="Required Rooms: ")
		self.rroom = wx.TextCtrl(self)
		vbox4.Add(self.rroomid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox4.Add(self.rroom,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox4,proportion=0,flag=wx.ALL,border=5)
		self.csizeid = wx.StaticText(self,label="          Class Size: ")
		self.csize = wx.TextCtrl(self)
		vbox5 = wx.BoxSizer(wx.HORIZONTAL)
		vbox5.Add(self.csizeid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox5.Add(self.csize,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox5,proportion=0,flag=wx.ALL,border=5)
		self.destimeid = wx.StaticText(self,label="    Desired Times: ")
		self.destime = wx.TextCtrl(self)
		vbox6 = wx.BoxSizer(wx.HORIZONTAL)
		vbox6.Add(self.destimeid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox6.Add(self.destime,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox6,proportion=0,flag=wx.ALL,border=5)
		self.submit = wx.Button(self,-1,'Submit')
		hbox.Add(self.submit,proportion=0,flag=wx.ALIGN_CENTER,border=5)
		
		self.Bind(wx.EVT_BUTTON,self.insConst,self.submit)
		
		self.SetSizer(hbox)
		hbox.Fit(self)	
		
	###########################################################################
	# insConst(self,e)
	# Description:
	#   This method takes the data the user input and inserts it into the constraint
	#   listctrl widget.
	###########################################################################
	def insConst(self,e):
		self.tp.constPage.insertConstraint(self.sname.GetValue(),self.course.GetValue(),self.rroom.GetValue(),self.csize.GetValue(),self.destime.GetValue())
		self.Close(True)

class InsertCourseDia(wx.Dialog):
	###########################################################################
	# __init__(self,parent,id,title)
	# Description:
	#   Constructor for the InsertRoomClass.
	# Input Parameters:
	#   title - title for the dialog window.
	###########################################################################
	def __init__(self,parent,id,title):
		self.tp = parent
		wx.Dialog.__init__(self,parent,id,title)
		self.panel = wx.Panel(self,-1)
		hbox = wx.BoxSizer(wx.VERTICAL)
		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.snameid = wx.StaticText(self,label="Professor: ")
		self.sname = wx.TextCtrl(self)
		vbox1.Add(self.snameid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox1.Add(self.sname,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox1,proportion=0,flag=wx.ALL,border=5)
		vbox2 = wx.BoxSizer(wx.HORIZONTAL)
		self.courseId = wx.StaticText(self,label="    Course: ")
		self.course = wx.TextCtrl(self)
		vbox2.Add(self.courseId,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox2.Add(self.course,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox2,proportion=0,flag=wx.ALL,border=5)
		vbox4 = wx.BoxSizer(wx.HORIZONTAL)
		self.rroomid = wx.StaticText(self,label="     Rooms: ")
		self.rroom = wx.TextCtrl(self)
		vbox4.Add(self.rroomid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox4.Add(self.rroom,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox4,proportion=0,flag=wx.ALL,border=5)
		self.destimeid = wx.StaticText(self,label="       Times: ")
		self.destime = wx.TextCtrl(self)
		vbox6 = wx.BoxSizer(wx.HORIZONTAL)
		vbox6.Add(self.destimeid,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox6.Add(self.destime,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=5)
		hbox.Add(vbox6,proportion=0,flag=wx.ALL,border=5)
		self.submit = wx.Button(self,-1,'Submit')
		hbox.Add(self.submit,proportion=0,flag=wx.ALIGN_CENTER,border=5)
		
		self.Bind(wx.EVT_BUTTON,self.insCourse,self.submit)
		
		self.SetSizer(hbox)
		hbox.Fit(self)	
		
	###########################################################################
	# insCourse(self,e)
	# Description:
	#   This method takes the data the user input and inserts it into the course
	#   listctrl widget.
	###########################################################################
	def insCourse(self,e):
		self.tp.schedPage.insertCourse(self.sname.GetValue(),self.course.GetValue(),self.rroom.GetValue(),self.destime.GetValue())
		self.Close(True)

		
###############################################################################
# InsertTimeDia(wx.Dialog)
# Description:
#   This class is used to create the Insert Time Dialog.
###############################################################################
class InsertTimeDia(wx.Dialog):
	###########################################################################
	# __init__(self,parent,id,title)
	# Description:
	#   Constructor for the InsertTimeClass.
	# Input Parameters:
	#   title - title for the dialog window.
	###########################################################################
	def __init__(self,parent,id,title):
		self.tp = parent
		wx.Dialog.__init__(self,parent,id,title)
		self.panel = wx.Panel(self,-1)
		hbox = wx.BoxSizer(wx.VERTICAL)
		vbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.timeLab = wx.StaticText(self,label="Time: ")
		self.time = wx.TextCtrl(self)
		vbox1.Add(self.timeLab,proportion=0,flag=wx.ALIGN_LEFT|wx.LEFT,border=5)
		vbox1.Add(self.time,proportion=0,flag=wx.ALIGN_RIGHT,border=5)
		hbox.Add(vbox1,proportion=0,flag=wx.ALL,border=5)
		self.submit = wx.Button(self,-1,'Submit')
		hbox.Add(self.submit,proportion=0,flag=wx.ALIGN_CENTER,border=5)
		
		self.Bind(wx.EVT_BUTTON,self.insertTime,self.submit)
		
		self.SetSizer(hbox)
		hbox.Fit(self)	
		
	###########################################################################
	# insertTime(self,e)
	# Description:
	#   This method takes the data the user input and inserts it into the time
	#   listctrl widget.
	###########################################################################
	def insertTime(self,e):
		self.tp.timePage.insertTime(self.time.GetValue())
		self.Close(True)
		
class ListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin, listmix.TextEditMixin):
	def __init__(self,parent):
		wx.ListCtrl.__init__(self,parent,-1,style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)
		listmix.TextEditMixin.__init__(self)

###############################################################################
# constraintsPage(wx.Panel)
# Description:
#   This displays all of the constraints in a listctrl widget.
###############################################################################
class constraintsPage(wx.Panel):
	###########################################################################
	# __init__(self,parent)
	# Description:
	#   Constructor.
	###########################################################################
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,size=(400,400))
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.list = ListCtrl(self)
		self.list.InsertColumn(0,'Professor',width=75)
		self.list.InsertColumn(1,'Course',width=75)
		self.list.InsertColumn(2,'Required Room',width=90)
		self.list.InsertColumn(3,'Required Class Size',width=130)
		self.list.InsertColumn(4,'Desired Time',width=100)
		hbox.Add(self.list,1,wx.EXPAND)
		
		self.list.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.deleteMenu)

		self.SetSizer(hbox)
		
	###########################################################################
	# deleteMenu(self,e)
	# Description:
	#   brings up the delete menu.
	###########################################################################
	def deleteMenu(self,e):
		self.PopupMenu(DeletePopupMenu(self), e.GetPosition())
		
	###########################################################################
	# delete(self)
	# Description:
	#   This will delete an entry from the listctrl.
	###########################################################################
	def delete(self):
		item = self.list.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		self.list.DeleteItem(item)
		
	###########################################################################
	# insertConstraint(self,prof,course,rooms,size,times)
	# Description:
	#   This inserts a constraint into the constraint listctrl page.
	# Input Parameters:
	#   prof - Professor short name.
	#   course - The course ID.
	#   rooms - Requested rooms.
	#   size - Expected class size.
	###########################################################################
	def insertConstraint(self,prof,course,rooms,size,times):
		index = self.list.InsertStringItem(sys.maxint, prof)
		self.list.SetStringItem(index, 1, course)
		self.list.SetStringItem(index, 2, rooms)
		self.list.SetStringItem(index, 3, size)
		self.list.SetStringItem(index, 4, times)

###############################################################################
# roomsPage(wx.Panel)
# Description:
#   This displays the rooms in a listctrl widget.
###############################################################################
class roomsPage(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,size=(400,400))
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.list = ListCtrl(self)
		self.list.InsertColumn(0,'RoomID',width=75)
		self.list.InsertColumn(1,'Class Size',width=75)
		hbox.Add(self.list,1,wx.EXPAND)
		self.list.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.deleteMenu)
		self.SetSizer(hbox)

	###########################################################################
	# deleteMenu(self,e)
	# Description:
	#   brings up the delete menu.
	###########################################################################
	def deleteMenu(self,e):
		self.PopupMenu(DeletePopupMenu(self), e.GetPosition())
		
	###########################################################################
	# delete(self)
	# Description:
	#   This will delete an entry from the listctrl.
	###########################################################################
	def delete(self):
		item = self.list.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		self.list.DeleteItem(item)

	###########################################################################
	# insertRoom(self,roomID,classSize)
	# Description:
	#   This inserts a room into the room listCtrl page.
	# Input Parameters:
	#   roomID - The room Id.
	#   classSize - Number of students the class can handle.
	###########################################################################
	def insertRoom(self,roomID,classSize):
		index = self.list.InsertStringItem(sys.maxint, roomID)
		self.list.SetStringItem(index, 1, classSize)

###############################################################################
# DeletePopupMenu(wx.Menu)
# Description:
#   Popup delete menu used to delete elements from each of the listctrl widgets.
###############################################################################
class DeletePopupMenu(wx.Menu):
	def __init__(self,parent):
		wx.Menu.__init__(self)
		self.parent = parent
		
		toDelete = wx.MenuItem(self,wx.NewId(), "delete")
		self.AppendItem(toDelete)
		self.Bind(wx.EVT_MENU,self.delete,id=toDelete.GetId())
		
	def delete(self,e):
		self.parent.delete()
		
###############################################################################
# schedulePage(wx.Panel)
# Description:
#   This displays the final schedule in a listctrl widget.
###############################################################################
class schedulePage(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.list = ListCtrl(self)
		self.list.InsertColumn(0,'Professor',width=75)
		self.list.InsertColumn(1,'Course',width=75)
		self.list.InsertColumn(2,'Room',width=100)
		self.list.InsertColumn(3,'Time',width=130)
		hbox.Add(self.list,1,wx.EXPAND)
		self.list.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.deleteMenu)
		self.SetSizer(hbox)
		
	def insertCourse(self,prof,course,room,time):
		index = self.list.InsertStringItem(sys.maxint, prof)
		self.list.SetStringItem(index, 1, course)
		self.list.SetStringItem(index, 2, room)
		self.list.SetStringItem(index, 3, time)
		
	def deleteMenu(self,e):
		self.PopupMenu(DeletePopupMenu(self), e.GetPosition())
		
	def delete(self):
		item = self.list.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		self.list.DeleteItem(item)

###############################################################################
# timePage(wx.Panel)
# Description:
#   This displays possible times in a listctrl widget.
###############################################################################
class timePage(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.list = ListCtrl(self)
		self.list.InsertColumn(0,'Time',width=75)
		hbox.Add(self.list,1,wx.EXPAND)
		self.list.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.deleteMenu)
		self.SetSizer(hbox)
		
	def insertTime(self,time):
		index = self.list.InsertStringItem(sys.maxint, time)
		
	def deleteMenu(self,e):
		self.PopupMenu(DeletePopupMenu(self), e.GetPosition())
		
	def delete(self):
		item = self.list.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
		self.list.DeleteItem(item)
		
###############################################################################
# MainWindow(wx.Frame)
# Description:
#   This is basically the heart of the GUI. It is where the user will spend
#   his time. It gives access to all aspects of the app.
###############################################################################
class MainWindow(wx.Frame):
	def __init__(self,parent,title):
		self.dirname = ''
		self.filename = ''
		wx.Frame.__init__(self,parent,title=title,size=(500,400))
		self.CreateStatusBar()
		
		filemenu = wx.Menu()
		
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "About")
		filemenu.AppendSeparator()
		menuOpen = filemenu.Append(-1,"&Open Constraints","Open constraints file")
		roomOpen = filemenu.Append(-1,"Open Rooms","Open rooms file")
		timeOpen = filemenu.Append(-1,"Open Times","Open times file")
		scedSave = filemenu.Append(-1,"&Save Schedule","Save schedule")
		roomSave = filemenu.Append(-1,"Save Rooms","Save Rooms")
		timeSave = filemenu.Append(-1,"Save Times","Save Times")
		constSave = filemenu.Append(-1,"Save Constraints","Save Constraints")
		filemenu.AppendSeparator()		
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Close Program")
		
		runmenu = wx.Menu()
		menuRun = runmenu.Append(-1,"&Create Schedule","Create Schedule")
		
		insertmenu = wx.Menu()
		insRoommenu = insertmenu.Append(-1,"Insert Room","Insert Room")
		insConstraint = insertmenu.Append(-1,"Insert Constraint","Insert Constraint")
		insCourse = insertmenu.Append(-1,"Insert Course","Insert Course")
		insTime = insertmenu.Append(-1,"Insert Time","Insert Time")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		menuBar.Append(insertmenu,"&Insert")
		menuBar.Append(runmenu,"&Run")
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU,self.onAbout,menuAbout)
		self.Bind(wx.EVT_MENU,self.saveSchedule,scedSave)
		self.Bind(wx.EVT_MENU,self.onExit,menuExit)
		self.Bind(wx.EVT_MENU,self.onOpen,menuOpen)
		self.Bind(wx.EVT_MENU,self.onOpenRooms,roomOpen)
		self.Bind(wx.EVT_MENU,self.onOpenTimes,timeOpen)
		self.Bind(wx.EVT_MENU,self.insertRoom,insRoommenu)
		self.Bind(wx.EVT_MENU,self.insertTime,insTime)
		self.Bind(wx.EVT_MENU,self.saveRooms,roomSave)
		self.Bind(wx.EVT_MENU,self.saveTimes,timeSave)
		self.Bind(wx.EVT_MENU,self.saveConsts,constSave)
		self.Bind(wx.EVT_MENU,self.createSched,menuRun)
		self.Bind(wx.EVT_MENU,self.insertConstraint,insConstraint)
		self.Bind(wx.EVT_MENU,self.insertCourse,insCourse)
		
		self.panel = wx.Panel(self)
		self.nb = wx.Notebook(self.panel)
		self.constPage = constraintsPage(self.nb)
		self.schedPage = schedulePage(self.nb)
		self.roomPage = roomsPage(self.nb)
		self.timePage = timePage(self.nb)
		
		self.nb.AddPage(self.constPage,"Constraints Page")
		self.nb.AddPage(self.schedPage,"Schedule Page")
		self.nb.AddPage(self.roomPage,"Rooms Page")
		self.nb.AddPage(self.timePage,"Times Page")
		
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.nb,1,wx.EXPAND)
		self.panel.SetSizer(sizer)
		
		
		
		self.Show(True)
	
###############################################################################
# createSched(self,e)
# Description:
# This takes the input from the constPage, roomPage, and timePage and sends
# it to the genetic algorithm to create a schedule. It then sends the outputed
# schedule the the schedPage.
###############################################################################
	def createSched(self,e):
		initial = []
		times = []
		rooms = []
		for i in range(0,self.roomPage.list.GetItemCount()):
			item = self.roomPage.list.GetItem(i,0)
			rooms.append(item.GetText())
			
		for i in range(0,self.timePage.list.GetItemCount()):
			item = self.timePage.list.GetItem(i,0)
			times.append(item.GetText())
			
		for i in range(0,self.constPage.list.GetItemCount()):
			item = self.constPage.list.GetItem(i,1)
			initial.append(item.GetText())
			item = self.constPage.list.GetItem(i,0)
			initial.append(item.GetText())
			
			item = self.constPage.list.GetItem(i,4)
			initial.append(item.GetText().split(','))
			
			item = self.constPage.list.GetItem(i,2)
			initial.append(item.GetText().split(','))
			
			item = self.constPage.list.GetItem(i,3)
			initial.append(item.GetText())
		
		schedule = main.genAlg(self.constPage.list.GetItemCount(),initial,100,times,rooms,1000,False)
		print schedule
		for i in range(0,len(schedule),7):
			self.schedPage.insertCourse(schedule[i+3],schedule[i+2],schedule[i+1],schedule[i])
	
	def saveSchedule(self,e):
		dlg = wx.FileDialog(self,"Choose the Schedule File",self.dirname,"","*.*",wx.SAVE)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'w')
			consts = []
			i = 0
			for i in range(0,self.schedPage.list.GetItemCount()):
				item = self.schedPage.list.GetItem(i,0)
				file.write("\n"+item.GetText()+",")
				item = self.schedPage.list.GetItem(i,1)
				file.write(item.GetText()+",")
				item = self.schedPage.list.GetItem(i,2)
				file.write(item.GetText()+",")
				item = self.schedPage.list.GetItem(i,3)
				file.write(item.GetText())
			file.close()
		dlg.Close()	

###############################################################################
# saveRooms(self,e)
# Description:
#   This method saves the rooms to a basic text file to be read later.
###############################################################################
	def saveRooms(self,e):
		dlg = wx.FileDialog(self,"Choose the Room File",self.dirname,"","*.*",wx.SAVE)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'w')
			consts = []
			i = 0
			for i in range(0,self.roomPage.list.GetItemCount()):
				item = self.roomPage.list.GetItem(i,0)
				file.write(item.GetText()+"\n")
				item = self.roomPage.list.GetItem(i,1)
				file.write(item.GetText()+"\n")
			file.close()
		dlg.Close()

###############################################################################
# saveTimes(self,e)
# Description:
#   This method saves the times to a basic text file to be read later.
###############################################################################		
	def saveTimes(self,e):
		dlg = wx.FileDialog(self,"Choose the Schedule File",self.dirname,"","*.*",wx.SAVE)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'w')
			consts = []
			i = 0
			for i in range(0,self.timePage.list.GetItemCount()):
				item = self.timePage.list.GetItem(i,0)
				file.write(item.GetText()+"\n")
			file.close()
		dlg.Close()
		
###############################################################################
# saveConsts(self,e)
# Description:
#   This method saves the constraints to a basic text file to be read later.
###############################################################################
	def saveConsts(self,e):
		dlg = wx.FileDialog(self,"Save Constraints",self.dirname,"","*.*",wx.SAVE)
		if(dlg.ShowModal() == wx.ID_OK):
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'w')
			consts = []
			i = 0
			for i in range(0,self.constPage.list.GetItemCount()):
				item = self.constPage.list.GetItem(i,0)
				file.write(item.GetText()+"\n")
				item = self.constPage.list.GetItem(i,1)
				file.write(item.GetText()+"\n")
				item = self.constPage.list.GetItem(i,2)
				file.write(item.GetText()+"\n")
				item = self.constPage.list.GetItem(i,3)
				file.write(item.GetText()+"\n")
				item = self.constPage.list.GetItem(i,4)
				file.write(item.GetText()+"\n")
			file.close()
		dlg.Close()
		
		
	def insertRoom(self,e):
		insRoom = InsertRoomDia(self,-1,'Insert Room')
		insRoom.ShowModal()
		insRoom.Destroy()
		
	def insertConstraint(self,e):
		insConst = InsertConstraintDia(self,-1,'Insert Constraint')
		insConst.ShowModal()
		insConst.Destroy()
		
	def insertCourse(self,e):
		insCourse = InsertCourseDia(self,-1,'Insert Course')
		insCourse.ShowModal()
		insCourse.Destroy()
	
	def insertTime(self,e):
		insTime = InsertTimeDia(self,-1,'Insert Time')
		insTime.ShowModal()
		insTime.Destroy()
	
###############################################################################
# onOpen(self,e)
# Description:
#   This method opens a constraints file.
###############################################################################
	def onOpen(self,e):
		dlg = wx.FileDialog(self,"Choose the Schedule File",self.dirname,"","*.*",wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'r')
			consts = []
			i = 0
			for line in file:
				if(i != 5):
					consts.append(line)
					i += 1
				else:
					self.constPage.insertConstraint(consts[0].rstrip(),consts[1].rstrip(),consts[2].rstrip(),consts[3].rstrip(),consts[4].rstrip())
					consts = []
					consts.append(line)
					i = 1
			self.constPage.insertConstraint(consts[0].rstrip(),consts[1].rstrip(),consts[2].rstrip(),consts[3].rstrip(),consts[4].rstrip())
			file.close()
		dlg.Close()
	
###############################################################################
# onOpenRooms(self,e)
# Description:
#   This method opens a rooms file.
###############################################################################	
	def onOpenRooms(self,e):
		dlg = wx.FileDialog(self,"Choose the Schedule File",self.dirname,"","*.*",wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'r')
			rooms = []
			i = 0
			for line in file:
				if(i != 2):
					rooms.append(line)
					i += 1
				else:
					self.roomPage.insertRoom(rooms[0].rstrip(),rooms[1].rstrip())
					rooms = []
					rooms.append(line)
					i = 1
			self.roomPage.insertRoom(rooms[0].rstrip(),rooms[1].rstrip())
			file.close()
		dlg.Close()

###############################################################################
# onOpenTimes(self,e)
# Description:
#   This method opens a time file.
###############################################################################
	def onOpenTimes(self,e):
		dlg = wx.FileDialog(self,"Save Times",self.dirname,"","*.*",wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			file = open(os.path.join(self.dirname, self.filename),'r')
			rooms = []
			i = 0
			for line in file:
				if(i != 1):
					rooms.append(line)
					i += 1
				else:
					self.timePage.insertTime(rooms[0].rstrip())
					rooms = []
					rooms.append(line)
					i = 1
			self.timePage.insertTime(rooms[0].rstrip())
			file.close()
		dlg.Close()
			
	
	def onAbout(self,e):
		info = wx.AboutDialogInfo()
        #info.SetIcon(wx.Icon('icons/hunter.png', wx.BITMAP_TYPE_PNG))
		info.SetName('Course Scheduler')
		info.SetVersion('0.01 Alpha')
		info.SetDescription("This application will take a set of courses with \
corrisponding constraints and creates a course schedule that satisfys\n\
those constraints. I created this for CSC450 Software Engineering class taught by \
Dr. Crawley at Georgetown College.")
		info.SetWebSite('http://www.georgetowncollege.edu')
		info.AddDeveloper('Anthony Rios')
		dlg = wx.AboutBox(info)
		
	def onExit(self,e):
		self.Close(True)

app = wx.App(True)
frame = MainWindow(None,"Course Scheduler")
app.MainLoop()