#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

from PyQt5 import QtCore, QtWidgets, QtGui
from gui import Ui_BioEECoinsMain
from os.path import isfile
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import time
import threading

from opalkelly import OpalKelly
import constants

class Coins(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		
		self.ui = Ui_BioEECoinsMain()
		self.device = OpalKelly()
		self.updateFlag = True
		self.iterateFlag = False
		self.displayNumber = 1

		pg.setConfigOption('background',(239,235,231))
		pg.setConfigOption('foreground','k')
		
		self.ui.setupUi(self)
		
		self.device.openDevice()
		self.device.configurePLL()
		self.device.loadFile('../FPGA/OKPythonSample.bit')
		self.device.tryConfiguration()
		
		self.initializeGUI()
	
	def initializeGUI(self):
		self.bondButtons()
		self.configureDisplays()
		self.ui.logWindow.setReadOnly(True)

	def configureDisplays(self):
		self.ui.display1.setMouseEnabled(x=True, y=False)
		self.ui.display2.setMouseEnabled(x=True, y=False)

	def bondButtons(self):
		self.ui.channel_sel_1.clicked.connect(self.respondChannel1)
		self.ui.channel_sel_2.clicked.connect(self.respondChannel2)
		self.ui.channel_sel_3.clicked.connect(self.respondChannel3)
		self.ui.channel_sel_4.clicked.connect(self.respondChannel4)
		self.ui.channel_sel_5.clicked.connect(self.respondChannel5)

	def respondChannel1(self):
		self.ui.logWindow.appendPlainText("Channel1 selected...")
		self.device.tryDisplay1()
 
	def respondChannel2(self):
		self.ui.logWindow.appendPlainText("Channel2 selected...")
		self.device.tryDisplay2()

	def respondChannel3(self):
		self.ui.logWindow.appendPlainText("Channel3 selected...")
		self.updateFlag = True
		if ( not(self.iterateFlag) ):
			self.iterateDisplay()
			self.iterateFlag = True
		
	def respondChannel4(self):
		self.ui.logWindow.appendPlainText("Channel4 selected...")
		self.updateFlag = False
		self.iterateFlag = False
	
	def respondChannel5(self):
		self.ui.logWindow.appendPlainText("Channel5 selected...")
		self.ui.display1.plot([1,2,3,4,5],[1,2,3,4,5])
		
	def iterateDisplay(self):
		if (self.displayNumber == 1):
			self.device.tryDisplay1()
			self.displayNumber = 2
		elif (self.displayNumber == 2):
			self.device.tryDisplay2()
			self.displayNumber = 1
		else :
			pass

		if (self.updateFlag):
			threading.Timer(1, self.iterateDisplay).start()

	def closeEvent(self, event):
		print "Killing auto-updating threads..."
		self.updateFlag = False
		print "Closing the connection to the Opal Kelly..."
		# Wait for the opal kelly components to clean itself properly
		# Otherwise core dump is likely to be raised
		time.sleep(1.1)
		event.accept()
		

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	myapp = Coins()
	myapp.show()
	result = app.exec_()

	# Wait for the opal kelly components to clean itself properly
	# Otherwise core dump is likely to be raised
	#time.sleep(0.1)

	sys.exit(result)

