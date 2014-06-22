#!/usr/bin/python

"""
Jun 20: Borjar fran scratch ;_;
Jun 22: Enklaste, daligaste textredigeraren nagonsin! DONE!
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

		newAction = QtGui.QAction('New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('You can\'t have too many text files ;)')
		newAction.triggered.connect(self.newFile)

		saveAction = QtGui.QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Saaaaave meeeee')
		saveAction.triggered.connect(self.saveFile)

		openAction = QtGui.QAction('Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Pick a file to edit')
		openAction.triggered.connect(self.openFile)

		closeAction = QtGui.QAction('Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Bye bye!')
		closeAction.triggered.connect(self.close)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(closeAction)

		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Wolf Howl Edit')
		self.show()

	def newFile(self):
		self.text.clear()

	def saveFile(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME'))
		f = open(filename, 'w')
		filedata = self.text.toPlainText()
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
