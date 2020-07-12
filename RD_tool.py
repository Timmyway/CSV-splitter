from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSortFilterProxyModel, QStringListModel, QRegExp, QModelIndex
from PyQt5.QtWidgets import QMessageBox, QCompleter, QDirModel, QComboBox, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QMovie
import sys
import datetime
import os
import design
import csv
import subprocess
import csv_cuter
from custom_widget import CustomWidget
import tim_custom_widget as custom_widget
from set_operation import SetOperation

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.setupUi(self)
		# Import Custom Widget class:
		self.widget = CustomWidget()
		self.center_mainwindow(w=500, h=125)
		self.file_separator = '\n'
		self.is_csv = False
		self.event_manage()
		self.gui_setup()
				

	def event_manage(self):
		self.btnProcess.clicked.connect(lambda: self.cut(mode='txt'))
		self.btnQuit.clicked.connect(lambda: self.widget.close_app(self))		
		self.btnBrowse.clicked.connect(lambda: self.browse(self.lineEditAdress, self.labSize))
		self.btnOpenLocation.clicked.connect(lambda: self.open_local_folder())
		# Browse files - difference
		self.btnBrowseOriginal.clicked.connect(lambda: self.browse(
			self.formOriginalPath, self.labSizeOriginal)
		)
		self.btnBrowseDedup.clicked.connect(lambda: self.browse(
			self.formDedupPath, self.labSizeDedup)
		)
		# Browse files - intersection
		self.btnBrowseOriginalIntersect.clicked.connect(lambda: self.browse(
			self.formOriginalPathIntersect, self.labSizeOriginalIntersect)
		)
		self.btnBrowseDedupIntersect.clicked.connect(lambda: self.browse(
			self.formDedupPathIntersect, self.labSizeDedupIntersect)
		)
		# Browse files - union
		self.btnBrowseOriginalUnion.clicked.connect(lambda: self.browse(
			self.formOriginalPathUnion, self.labSizeOriginalUnion)
		)
		self.btnBrowseDedupUnion.clicked.connect(lambda: self.browse(
			self.formDedupPathUnion, self.labSizeDedupUnion)
		)
		# Calculate difference
		self.btnCalculate.clicked.connect(lambda: self.calculate(operation='difference'))
		# Calculate intersection
		self.btnCalculateIntersect.clicked.connect(lambda: self.calculate('intersection'))
		# Calculate union
		self.btnCalculateUnion.clicked.connect(lambda: self.calculate('union'))

	def quick_open(self, fname):
		''' Quick open file, then return a list of all element according to separator '''
		print('Open file: ', fname)	
		with open(fname, 'r', encoding='utf-8') as f:
			# The goal is to get all elements inside a file where elements are separate by separator
			if fname.lower().endswith('.csv'):
				self.is_csv = True
				reader = csv.reader(f)				
				csv_list = [e[0] for e in reader if e[0] != '']
				return csv_list
			elif fname.lower().endswith('.txt'):
				self.is_csv = False
				reader = f.read()
				csv_list = [entry for entry in reader.split(self.file_separator) if entry != '']
				return csv_list
			else:
				self.msg_box(msg_text="Format not recognized", 
					msg_type=QMessageBox.Warning, 
					msg_title="File extension error", 
					autoclose=True, timeout=2500
				)

	def gui_setup(self):
		self.spinBoxNbMorceau.setMinimum(2)
		self.spinBoxNbMorceau.setMaximum(250)
		self.spinBoxNbMorceau.setValue(2)
		self.setWindowTitle('RD tool')
		self.setWindowIcon(QIcon('static/icone.ico'))
		# Experimentation:
		#self.lineEditAdress.isUndoAvailable(False)


	def center_mainwindow(self, w=1280, h=720):
		self.resize(w,h)
		size_ecran = QtWidgets.QDesktopWidget().screenGeometry()
		size_fenetre = self.geometry()
		self.move((size_ecran.width() - size_fenetre.width()) / 2, (size_ecran.height() - size_fenetre.height()) / 2)


	def msg_box(self, msg_text="", msg_title="", 
			msg_type=QMessageBox.Information, 
			need_value=False, 
			option_1=QMessageBox.Ok, option_2=QMessageBox.Cancel, 
			style_msg_box='''QMessageBox {background-color: #2AC777;}
			QMessageBox QLabel, QPushButton {color: #ffffff; font-family: verdana; font-size: 16px;}
			QMessageBox QPushButton {background-color: #333333; border-radius: 4px; padding: 2px;}
			QMessageBox QPushButton:hover {background-color: #4E6057;}
			''', autoclose=False, timeout=3000
		):
		# A popup that auto close after x (3 by default) seconds
		msg = custom_widget.TimedMessageBox()
		# Configure popup (icon, text, title...)
		msg.setIcon(msg_type)
		msg.setText(msg_text)
		msg.setWindowTitle(msg_title)
		if need_value:
			msg.setStandardButtons(option_1 | option_2)
		msg.setStyleSheet(style_msg_box)
		msg.show()
		if autoclose:
			msg.countdown_close(timeout)
		retval = msg.exec_()
		print(retval)
		return retval

	def cut(self, mode='csv'):
		''' Open file then cut into multiples parts (given by the user) '''
		# Get input file path and file output name from user thanks to the widgets
		fname = self.lineEditAdress.text()
		output_name = self.lineEditOutputName.text()
		if fname:
			with open(fname, 'r') as f:
				if mode == 'csv':
					reader = csv.reader(f)
					csv_list = [e[0] for e in reader]
				else:
					reader = f.read()
					csv_list = reader.split('\n')
			list_result = csv_cuter.cut(csv_list, self.spinBoxNbMorceau.value())
			txt_result_list = ['\n'.join(e) for e in list_result]
			if not output_name:
				output_name = 'Unknow name file'
			[
			# Save 
			csv_cuter.save('%s - %s - part%s.csv' % (output_name, 
				datetime.datetime.now().strftime('%Hh%Mm%Ss'), str(i+1) ), content=e) 
			for i,e in enumerate(txt_result_list)
			]
			self.open_local_folder()
			self.statusbar.showMessage('All tasks are processed', 3000)
		else:
			self.statusbar.showMessage('Empty path', 3000)	

	def calculate(self, operation='difference'):
		''' If file A has "abcd" and B has "ab", output should be "ab" '''
		# Retrieve file paths (both original and dedup)
		if operation == 'difference':
			original_path = self.formOriginalPath.text()
			dedup_path = self.formDedupPath.text()
		elif operation == 'intersection':
			original_path = self.formOriginalPathIntersect.text()
			dedup_path = self.formDedupPathIntersect.text()
		elif operation == 'union':
			original_path = self.formOriginalPathUnion.text()
			dedup_path = self.formDedupPathUnion.text()
		try:
			original_file = self.quick_open(original_path)
			dedup_file = self.quick_open(dedup_path)			
		except FileNotFoundError:
			self.msg_box(msg_text="File not found", 
				msg_type=QMessageBox.Warning, 
				msg_title="Dedup tool error", 
				autoclose=True, timeout=2500
			)
			return		
		# According to the kind of operation, decide to call the appropriate method
		set_operation = SetOperation(original_file, dedup_file)
		if operation == 'difference':
			set_operation.get_difference()
			result_set = set_operation.difference
		elif operation == 'intersection':
			set_operation.get_intersection()
			result_set = set_operation.intersection
		elif operation == 'union':
			set_operation.get_union()
			result_set = set_operation.union
		# Save result to the disk, then notify the user
		print('Result: = ', result_set)
		save_operation = self.save(self.file_separator.join(result_set))
		if save_operation == 'saved':
			self.msg_box(msg_text=f"{operation.capitalize()} calculation finished", 
				msg_type=QMessageBox.Information, msg_title="Dedup tool", 
				autoclose=True, timeout=2500
			)	

	def save(self, content):
		''' Popup a dialog to get the path, then save as file on disk '''
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', "","Text document(*.txt);;CSV file(*.csv)", options=options)
		if filename:
			with open(filename, 'w', encoding='utf-8') as f:
				f.write(content)
				return 'saved'

	def open_folder(self, path):		
		subprocess.run(['explorer', os.path.realpath(path)])

	def open_local_folder(self):
		location = os.getcwd()
		self.open_folder(location)

	def ask_dialog(self):
		options = QFileDialog.Options()
		current_dir = os.getcwd()
		filename, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', current_dir,
			"CSV file(*.csv);;Text document(*.txt);;All Files (*)", options=options)
		if filename:
			print(filename)
			return filename

	def fill_path(self, widget, text):
		if isinstance(widget, QLineEdit):
			widget.setText(text)

	def browse(self, line_edit, label=None):
		path = self.ask_dialog()
		if path:
			self.fill_path(line_edit, path)
			if label is not None:
				label.setText('%s Ko' % self.get_size(path))

	def get_size(self, path):
		''' Take a file path as input, calculate then return its size '''
		try:
			if path:
				size = round(os.path.getsize(path) / 1000)
				return size
		except FileNotFoundError:
			return 0
		

def main():
	app = QtWidgets.QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()