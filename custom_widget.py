from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QMovie, QKeySequence
from PyQt5.QtWidgets import QMessageBox, QAction, QColorDialog, QDesktopWidget,\
 QCompleter, QTableWidgetItem

class CustomWidget(object):
	"""docstring for CustomWidget"""
	def __init__(self):
		super(CustomWidget, self).__init__()
		pass
		

	def msg_box(self, msg_text="", msg_title="", msg_type=QMessageBox.Information, need_value=False):
			msg = QMessageBox()
			msg.setIcon(msg_type)
			msg.setText(msg_text)
			msg.setWindowTitle(msg_title)
			if need_value:
				msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
			msg.show()
			retval = msg.exec_()
			print(retval)
			return retval
			
	def close_app(self, parent, direct_quit=False):
		if not direct_quit:
			box = self.msg_box(msg_text="Do you really want to quit?", msg_title="Close application", 
				msg_type=QMessageBox.Question, need_value=True)
			if box == 1024:
				parent.close()
		else:
			self.close()