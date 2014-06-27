#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
Jun 20: Börjar från scratch ;_;
Jun 22: Enklaste, dåligaste textredigeraren någonsin! DONE!

TODO: Lägg till en QToolBar, setToolTip funkar ej i menyer
"""

import sys
import os
from PyQt4 import QtGui, QtCore


class UAEH(QtGui.QMainWindow):
	def __init__(self):
		super(UAEH, self).__init__()
		self.initUI()

	def initUI(self):

		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)

		QtGui.QToolTip.setFont(QtGui.QFont('Ubuntu', 10))

		newAction = QtGui.QAction(QtGui.QIcon('new.png'), 'New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setToolTip('You can\'t have too many text files ;)')
		newAction.triggered.connect(self.newFile)

		saveAction = QtGui.QAction(QtGui.QIcon('save.png'), 'Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setToolTip('Saaaaave meeeee')
		saveAction.triggered.connect(self.saveFile)

		openAction = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setToolTip('Pick a file to edit')
		openAction.triggered.connect(self.openFile)

		closeAction = QtGui.QAction(QtGui.QIcon('close.png'), 'Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setToolTip('Bye bye!')
		closeAction.triggered.connect(self.close)

		self.toolbar = self.addToolBar('O HAI!')
		self.toolbar.addAction(newAction)
		self.toolbar.addAction(openAction)
		self.toolbar.addAction(saveAction)
		self.toolbar.addAction(closeAction)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(closeAction)

		self.setGeometry(300, 300, 800, 640)
		self.setWindowTitle('Wolf Howl Edit')
		self.show()

	def newFile(self):
		self.text.clear()

	def saveFile(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME'))
		f = open(filename, 'w')
		filedata = self.text.toPlainText()
		if filedata is empty:
			errorbox = QMessageBox.critical("Critical", "Please enter text!")
		f.write(filedata)
		f.close()
	
	def openFile(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
		f = open(filename, 'r')
		filedata = f.read()
		self.text.setText(filedata)
		f.close()


def main():
	app = QtGui.QApplication(sys.argv)
	ulf = UAEH()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
