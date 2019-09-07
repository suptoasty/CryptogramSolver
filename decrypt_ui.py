#!/usr/bin/env python
from decryptorator5000 import read_text, print_list, solve, text_to_list, read_plain_text
import random
import sys
import types

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QLayout, QPushButton, QMainWindow, QFileDialog, QTextEdit

# !!! Im using an old pyqt5 file i used to learn qt5 !!!
#####
class app(QApplication):
    def __init__(self, args):
        QApplication.__init__(self, args)
        print("Arguments-> ", args)


class window(QWidget):
    __layout = QVBoxLayout()

    def __init__(self, widget: QWidget = None):
        QWidget.__init__(self)

        if(not widget is None):
            self.__layout.addWidget(widget)
        self.setLayout(self.__layout)

    def getLayout():
        return __layout


class wid(QWidget):
    __widgets = []
    __layout = QVBoxLayout()

    def __init__(self, widgets: [] = None, layout: QLayout = None):
        QWidget.__init__(self)
        if(not widgets is None):
            self.__widgets = widgets
        if(not layout is None):
            self.__layout = layout

        for i in self.__widgets:
            self.__layout.addWidget(i)
            print(i)
        self.setLayout(layout)

    def getLayout():
        return __layout

    # def _setLayout(layout: QLayout):
    #     self.__layout = layout
    #     QWidget.setLayout(layout)

    def getWidgets():
        return __widgets

    def pushWidget(widget: QWidget):
        __widgets.append(widget)
#####



# Driver Below
cipher: list = None
plaintext: list = None
def open_file(dia: QFileDialog, cipher_text: QTextEdit, plaintext_text: QTextEdit):
	file = dia.getOpenFileName()
	cipher = read_text(file[0])
	cipher_text.setText(read_plain_text(file[0]))

	plaintext = solve(text_to_list(cipher_text.toPlainText()))
	plaintext_text.setText(str(plaintext))

def solve_cipher(cipher_text: QTextEdit, plaintext_text: QTextEdit):
    if cipher_text.toPlainText() is "":
        print("No Text in Cipher object")
        sys.exit(1)
        return

    plaintext = solve(text_to_list(cipher_text.toPlainText()))
    plaintext_text.setText(str(plaintext))
    return plaintext


if __name__ == "__main__":
	# get commandline args and create new app
	m_app = app(sys.argv)
	
	# make new label and button for file selection
	m_button = QPushButton("Choose File")
	m_label = QLabel("Select File: ")
	
	m_cipher_text = QTextEdit("")
	# m_cipher_text.setDisabled(True)
	m_cipher_label = QLabel("Cipher: ")
	
	m_plain_text = QTextEdit("")
	m_plain_text.setDisabled(True)
	m_plaintext_label = QLabel("Plain Text: ")
	
	m_solve_btn = QPushButton("Solve")
	m_solve_btn.clicked.connect(lambda: solve_cipher(m_cipher_text, m_plain_text))

	# new layout widget
	m_widget = wid([m_label, m_button, m_cipher_label, m_cipher_text, m_plaintext_label, m_plain_text, m_solve_btn], QVBoxLayout())

	# new file chooser
	m_file_chooser = QFileDialog(m_widget, "Choose File", ".", "")
	m_button.clicked.connect(lambda: open_file(m_file_chooser, m_cipher_text, m_plain_text))
	
	# new window
	m_window = window(m_widget)
	m_window.show()
	
	# main loop till exit
	sys.exit(m_app.exec_())