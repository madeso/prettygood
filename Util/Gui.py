import App
from PySide import QtCore, QtGui

def information(message):
	QtGui.QMessageBox.information(None, App.instance.ReadableAppName, message)


def yesno(message):
	return QtGui.QMessageBox.question(None, App.instance.ReadableAppName, message) == 0

def error(p):
	QtGui.QMessageBox.critical(None, App.instance.ReadableAppName, message)

def warning(p):
	QtGui.QMessageBox.warning(None, App.instance.ReadableAppName, message)