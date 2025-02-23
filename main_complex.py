import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import serial
import pyautogui
import time
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 700)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("rgb(222831)")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 10, 541, 681))
        self.label.setStyleSheet("background-color: rgb(34, 40, 49);\n"
"border-radius: 20px; ")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.func_display = QtWidgets.QLabel(self.widget)
        self.func_display.setGeometry(QtCore.QRect(120, 180, 281, 71))
        self.func_display.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.func_display.setFocus()

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.func_display.setFont(font)
        self.func_display.setStyleSheet("color: rgb(255, 255, 255);")
        self.func_display.setObjectName("func_display")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 350, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        
        
        
        self.on_btn = QtWidgets.QPushButton(self.widget)
        self.on_btn.setGeometry(QtCore.QRect(110, 460, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.on_btn.setFont(font)
        self.on_btn.setObjectName("on_btn")
        self.off_btn = QtWidgets.QPushButton(self.widget)
        self.off_btn.setGeometry(QtCore.QRect(320, 460, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.off_btn.setFont(font)
        self.off_btn.setObjectName("off_btn")
        self.on_btn.clicked.connect(self.send_1)
        self.off_btn.clicked.connect(self.send_0)

        # 2 list giá trị thay đổi lần lượt 
        self.skills1 = ['Up', 'Down', 'Left', 'Right']
        self.skills2 = ['Lên', 'Xuống', 'Trái', 'Phải']
        self.current_skills = self.skills1  # Khởi tạo các kỹ năng hiện tại
        self.show_skill = ''


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget.setFocus()
        self.func_display.setFocusPolicy(Qt.StrongFocus)

        Form.keyPressEvent = self.keyPressEvent
        Form.mousePressEvent = self.mousePressEvent
        

        self.serial_control = SerialControl('COM9')


    # def openSerialPort(self):
    #     self.ser = serial.Serial('COM9', 9600, timeout=1)
    #     print("Running")
    #     print('_'*30)


    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.func_display.setText(self.current_skills[0])
            self.show_skill = self.current_skills[0]
            print(self.show_skill)


        elif event.key() == Qt.Key_Down:
            self.func_display.setText(self.current_skills[1])
            self.show_skill = self.current_skills[1]
            print(self.show_skill)


        elif event.key() == Qt.Key_Left:
            self.func_display.setText(self.current_skills[2])
            self.show_skill = self.current_skills[2]
            print(self.show_skill)


        elif event.key() == Qt.Key_Right:
            self.func_display.setText(self.current_skills[3])
            self.show_skill = self.current_skills[3]
            print(self.show_skill)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.current_skills == self.skills1:  # Nếu đang hiển thị skill set 1, chuyển sang skill set 2
                self.current_skills = self.skills2
            else:  # Nếu đang hiển thị skill set 2, chuyển sang skill set 1
                self.current_skills = self.skills1
            self.func_display.setText('Skill Set Changed')



    # def send_data(value):
    #     if value in ['0', '1']:
    #         ser.write(value.encode('utf-8'))  # Gửi chuỗi qua serial
    #         print("Send:", value)
    #     else:
    #         print("Invalid input. Please enter 0 or 1.")

    def send_1(self):
        
        self.serial_control.send_data('1')

    def send_0(self):
            
        self.serial_control.send_data('0')



        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Funtcion Selection"))
        self.label_2.setText(_translate("Form", "Select Function: "))
        self.label_3.setText(_translate("Form", "Show Function Key:"))
        self.func_display.setText(_translate("Form", "Key Press: "))
        self.label_5.setText(_translate("Form", "Send Signal (0,1):"))
        self.on_btn.setText(_translate("Form", "ON"))
        self.off_btn.setText(_translate("Form", "OFF"))


class SerialControl:
    def __init__(self, port):
        self.port = port
        self.ser = None
        self.initialize_serial()

    def initialize_serial(self):
        try:
            self.ser = serial.Serial(self.port, 9600, timeout=3)
            print("Serial port opened successfully.")
        except serial.SerialException as e:
            print("SerialException:", e)
        except Exception as ex:
            print("Exception:", ex)

    def send_data(self, value):
        if self.ser is not None and self.ser.is_open:
            try:
                self.ser.write(value.encode('utf-8'))
                print("Send:", value)
            except Exception as e:
                print("Error sending data:", e)
        else:
            print("Serial port is not open or initialized.")

    def receive_data(self):
        while True:
            if self.ser is not None and self.ser.is_open:
                try:
                    data = self.ser.readline().decode('utf-8').rstrip()
                    if data == 'UP' or data == 'Button 3: 1':
                        pyautogui.press('up')
                    elif data == 'DOWN' or data == 'Button 4: 1':
                        pyautogui.press('down')
                    elif data == 'LEFT'  or data == 'Button 1: 1':
                        pyautogui.press('left')
                    elif data == 'RIGHT' or data == 'Button 2: 1':
                        pyautogui.press('right')
                except Exception as e:
                    print("Error receiving data:", e)
            else:
                print("Serial port is not open or initialized.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # Thiết lập và khởi chạy luồng giao tiếp serial
    serial_control = SerialControl('COM9')
    send_data_thread = threading.Thread(target=serial_control.send_data)
    serial_control_thread = threading.Thread(target=ui.serial_control.receive_data)
    serial_control_thread.start()

    
    send_data_thread.start()
    #receive_thread.start()

    sys.exit(app.exec_())
