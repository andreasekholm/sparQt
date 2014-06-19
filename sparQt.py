#!/usr/bin/python
# -*- coding: cp865 -*-

"""
Jun 17: Fonster skapas.
Jun 18: Knapp tillagd. Knappen stanger fonstret. Tooltip funkar.
Jun 19: Fuck fonster! Edit: Works!
"""

import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()

		self.initUI()

		# bestäm typsnitt för programmet
	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('Ubuntu', 10))

		# self.setToolTip() - tooltip i hela fönstret @_@

		btn = QtGui.QPushButton('Kuddfluffaren!', self)
		btn.setToolTip('Denna knapp <u>stänger</u> fönstret!')
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(btn.sizeHint())
		btn.move(300, 100)

		# sätt fönsterstorlek
		self.setGeometry(300, 300, 450, 150)
		self.setWindowTitle('Ulf Window')
		self.setWindowIcon(QtGui.QIcon('web.png'))

		self.show()

		# skapar en dialog om du verkligen vill stänga fönstret
	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Message', "Are you quitting?", 
			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()