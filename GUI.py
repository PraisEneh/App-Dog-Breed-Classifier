# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, save_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from PIL import Image, ImageGrab
import numpy as np
import cv2
import ast
import os

# TEST_DIR = "test/"
# CATEGORIES = [folder for folder in os.listdir(TEST_DIR)]
with open('categories.txt', 'r') as file:
    content = file.read()

# Convert the string to a list
CATEGORIES = ast.literal_eval(content)
model = load_model('model/FT_RR-20_ZR-0.5_LR-0.0001_CLR-False_LR-0.001-CL-6-Drop-0.2-FSize-512-07_28_42.h5')

class Ui_MainWindow(object):
    def __init__(self):
        self.filename = None

    def setupDogDatabaseLabel(self):
        # Load categories from a file
        with open('categories.txt', 'r') as file:
            categories = ast.literal_eval(file.read())

        # Format the categories into HTML list items
        formatted_categories = '<br>- '.join(categories)

        # Create a QLabel to contain the text
        label_content = QtWidgets.QLabel()
        label_content.setText(f"""<html><head/><body>
        <p><span style=" font-size:11pt; text-decoration: underline;">Dog Database:</span></p>
        <p><span style=" font-size:9pt;">- {formatted_categories}</span></p>
        </body></html>""")
        label_content.setTextFormat(QtCore.Qt.RichText)
        label_content.setWordWrap(True)

        # Create a QScrollArea
        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(10, 330, 371, 211))  # Set to the same dimensions as the original label
        self.scroll_area.setWidget(label_content)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Disable horizontal scroll
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)  # Enable vertical scroll only when needed


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1598, 759)
        #MainWindow.setMinimumSize(1920, 1080)
        #MainWindow.setMaximumSize(1920, 1080)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 10, 611, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("default_dog.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.get_image_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_image_btn.setGeometry(QtCore.QRect(20, 70, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.get_image_btn.setFont(font)
        self.get_image_btn.setObjectName("get_image_btn")
        self.get_image_btn.clicked.connect(self.getImage)
        self.detect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detect_btn.setGeometry(QtCore.QRect(250, 70, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.detect_btn.setFont(font)
        self.detect_btn.setIconSize(QtCore.QSize(24, 24))
        self.detect_btn.setObjectName("detect_btn")
        self.detect_btn.clicked.connect(self.detectImage)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 600, 841, 131))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1170, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(1170, 230, 281, 31))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.label_4.setFont(font)
        # self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1170, 410, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getScreenshot)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 330, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.nameTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameTextEdit.setGeometry(QtCore.QRect(1170, 70, 391, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nameTextEdit.setFont(font)
        self.nameTextEdit.setReadOnly(True)
        self.nameTextEdit.setObjectName("nameTextEdit")
        # self.percentTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        # self.percentTextEdit.setGeometry(QtCore.QRect(1170, 260, 391, 131))
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.percentTextEdit.setFont(font)
        # self.percentTextEdit.setReadOnly(True)
        # self.percentTextEdit.setPlainText("")
        # self.percentTextEdit.setObjectName("percentTextEdit")
        self.othersTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.othersTextEdit.setGeometry(QtCore.QRect(1170, 440, 391, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.othersTextEdit.setFont(font)
        self.othersTextEdit.setReadOnly(True)
        self.othersTextEdit.setPlainText("")
        self.othersTextEdit.setObjectName("othersTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getImage(self):
        print("Hi")
        self.filename = askopenfilename()
        print("Type: ", type(self.filename))
        if self.filename:
            self.label.setPixmap(QtGui.QPixmap(self.filename))

    def detectImage(self):
        if self.filename:
            img = cv2.imread(self.filename)
            img = cv2.resize(img, (128, 128))  # Resize as per model's input
            img = img.astype('float32') / 255.0  # Normalize
            img = np.expand_dims(img, axis=0)  # Add batch dimension

            predictions = model.predict(img)
            print("Raw predictions:", predictions)
            
            # Get the indices of the top 3 predictions
            top_3_indices = np.argsort(predictions[0])[-3:][::-1]
            
            # Prepare text for UI update
            top_classes = [CATEGORIES[idx] for idx in top_3_indices]
            top_probabilities = predictions[0][top_3_indices]
            
            top_1_text = f"{top_classes[0]}: {top_probabilities[0] * 100:.2f}%"
            top_2_text = f"{top_classes[1]}: {top_probabilities[1] * 100:.2f}%"
            top_3_text = f"{top_classes[2]}: {top_probabilities[2] * 100:.2f}%"

            # Update the UI with the top prediction
            self.nameTextEdit.setPlainText(top_1_text)
            
            # Use othersTextEdit to show the top 2 and top 3 predictions
            self.othersTextEdit.setPlainText(f"{top_2_text}\n{top_3_text}")

    def getTop(self, detects):
        for i, j in detects:
            if i > i - 1:
                top = [i, j]
        return top

    def getTop3(self, detects):
        sortlist = sorted(detects, reverse=True)[:3]
        return sortlist

    def getScreenshot(self):
        print('method')
        size = MainWindow.size()
        img = ImageGrab.grab(bbox=(MainWindow.x(), MainWindow.y(), size.width()+MainWindow.x(), size.height()+MainWindow.y()))
        img.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dog Identifier"))
        self.get_image_btn.setText(_translate("MainWindow", "Choose Image"))
        self.detect_btn.setText(_translate("MainWindow", "Detect"))
        self.label_2.setText(_translate("MainWindow", "The Dog Identifier"))
        self.label_3.setText(_translate("MainWindow", "Chances are this is a..."))
        # self.label_4.setText(_translate("MainWindow", "with a likelyhood of..."))
        self.label_5.setText(_translate("MainWindow", "Other notable predictions."))
        self.label_6.setText(_translate("MainWindow", "Choose an image of a dog to detect."))
        self.pushButton.setText(_translate("MainWindow", "Save Context"))
        self.setupDogDatabaseLabel()
        self.nameTextEdit.setPlainText(_translate("MainWindow", "dog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())