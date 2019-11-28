from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSortFilterProxyModel, QStringListModel, QRegExp, QModelIndex
from PyQt5.QtWidgets import QMessageBox, QCompleter, QDirModel, QComboBox, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QMovie
# from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import datetime
import os
import design
import csv
import subprocess
import csv_cuter
from custom_widget import CustomWidget
import tim_custom_widget as custom_widget
import set_difference
from configure import read_json

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.setupUi(self)
		# Import Custom Widget class:
		self.widget = CustomWidget()
		self.center_mainwindow(w=500, h=125)
		config_file = read_json('config')
		self.user_setting = config_file['user_preference']
		self.file_separator = '\n'
		self.is_csv = False
		self.event_manage()
		self.gui_setup()
				

	def event_manage(self):
		self.btnProcess.clicked.connect(lambda: self.cut(mode='txt'))
		self.btnQuit.clicked.connect(lambda: self.widget.close_app(self))		
		self.btnBrowse.clicked.connect(lambda: self.browse(self.lineEditAdress, self.labSize))
		self.btnOpenLocation.clicked.connect(lambda: self.open_local_folder())
		self.btnBrowseOriginal.clicked.connect(lambda: self.browse(self.formOriginalPath, self.labSizeOriginal))
		self.btnBrowseDedup.clicked.connect(lambda: self.browse(self.formDedupPath, self.labSizeDedup))
		self.btnCalculate.clicked.connect(lambda: self.calculate())

	def quick_open(self, fname):
		with open(fname, 'r', encoding='utf-8') as f:
			if fname.endswith(('.CSV', '.Csv', '.CSv', 'cSV', 'cSv', 'csv', 'csV', 'CsV')):
				self.is_csv = True
				reader = csv.reader(f)
				csv_list = [e[0] for e in reader]
				return csv_list
			elif fname.endswith(('.TXT', '.Txt', '.TXt', 'tXT', 'tXt', 'txt', 'txT', 'TxT')):
				self.is_csv = False
				reader = f.read()
				csv_list = reader.split(self.file_separator)
				return csv_list
			else:
				self.msg_box(msg_text="Format not recognized", msg_type=QMessageBox.Warning, msg_title="File extension error", autoclose=True, timeout=2500)

	def gui_setup(self):
		max_split = self.user_setting['max_split']
		self.spinBoxNbMorceau.setMinimum(2)
		self.spinBoxNbMorceau.setMaximum(max_split if max_split < 100000 else 100000)
		self.spinBoxNbMorceau.setValue(self.user_setting['num_split'])
		# Experimentation:
		#self.lineEditAdress.isUndoAvailable(False)


	def center_mainwindow(self, w=1280, h=720):
		self.resize(w,h)
		size_ecran = QtWidgets.QDesktopWidget().screenGeometry()
		size_fenetre = self.geometry()
		self.move((size_ecran.width() - size_fenetre.width()) / 2, (size_ecran.height() - size_fenetre.height()) / 2)


	def msg_box(self, msg_text="", msg_title="", msg_type=QMessageBox.Information, need_value=False, option_1=QMessageBox.Ok, 
		option_2=QMessageBox.Cancel, style_msg_box='''QMessageBox {background-color: #2AC777;}
		QMessageBox QLabel, QPushButton {color: #ffffff; font-family: verdana; font-size: 16px;}
		QMessageBox QPushButton {background-color: #333333; border-radius: 4px; padding: 2px;}
		QMessageBox QPushButton:hover {background-color: #4E6057;}
		''', autoclose=False, timeout=3000):
		msg = custom_widget.TimedMessageBox()
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
			csv_cuter.save('%s - %s - part%s.csv' % (output_name, 
				datetime.datetime.now().strftime('%Hh%Mm%Ss'), str(i+1) ), content=e) 
			for i,e in enumerate(txt_result_list)
			]
			self.open_local_folder()
			self.statusbar.showMessage('All tasks are processed', 3000)
		else:
			self.statusbar.showMessage('Empty path', 3000)

	def calculate(self):
		original_path = self.formOriginalPath.text()
		dedup_path = self.formDedupPath.text()
		try:
			original_file = self.quick_open(original_path)
			dedup_file = self.quick_open(dedup_path)
		except FileNotFoundError:
			self.msg_box(msg_text="File not found", msg_type=QMessageBox.Warning, msg_title="Dedup tool error", autoclose=True, timeout=2500)
			return
		if self.is_csv:
			original_set = set(original_file)
			dedup_set = set(dedup_file)

		else:
			original_set = set(original_file)
			dedup_set = set(dedup_file)
		result_set = original_set - dedup_set
		self.save(self.file_separator.join(result_set))
		self.msg_box(msg_text="Finished", msg_type=QMessageBox.Information, msg_title="Dedup tool", autoclose=True, timeout=2500)	

	def save(self, content):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', "","Text document(*.txt);;CSV file(*.csv)", options=options)
		if filename:
			with open(filename, 'w', encoding='utf-8') as f:
				f.write(content)
				self.msg_box(msg_text="Saved", msg_type=QMessageBox.Information, msg_title="Dedup tool", autoclose=True, timeout=2000)

	def open_folder(self, path):		
		subprocess.run(['explorer', os.path.realpath(path)])

	def open_local_folder(self):
		location = os.getcwd()
		self.open_folder(location)

	def ask_dialog(self):
		options = QFileDialog.Options()
		current_dir = os.getcwd()
		filename, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', current_dir,
			"CSV file(*.csv);;CSV file(*.txt);;All Files (*)", options=options)
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