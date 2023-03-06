from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
class CustomCalculator(QMainWindow):
    def __init__(self):
        super(CustomCalculator, self).__init__()
        loadUi('calc.ui', self)
        self.add.clicked.connect(self.add_bottun)
        self.sub.clicked.connect(self.sub_bottun)
        self.mult.clicked.connect(self.mult_button)
        self.div.clicked.connect(self.div_button)
    
    def add_bottun(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 + num2}")
        except:
            self.result.setText("Введи цифры")
    def sub_bottun(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 - num2}")
        except:
            self.result.setText("Введи цифры")
    def mult_button(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 * num2}")
        except:
            self.result.setText("Введи цифры")
    def div_button(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            try:
                self.result.setText(f"Ответ: {num1 / num2}")
            except:
                self.result.setText("на ноль нельзя делить")
        except:
            self.result.setText("Введи цифры")
app = QApplication(sys.argv)
calc = CustomCalculator()
calc.show()
app.exec_()