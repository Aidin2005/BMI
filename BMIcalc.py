from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QGridLayout
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt
import sys


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 350)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        self.label_weight = QLabel("Weight (kg):")
        self.label_weight.setStyleSheet("color: #333;")
        layout.addWidget(self.label_weight, 0, 0)


        self.input_weight = QLineEdit()
        self.input_weight.setValidator(QDoubleValidator())
        self.input_weight.setStyleSheet("color: black;")  # Черный текст
        layout.addWidget(self.input_weight, 0, 1)

        self.label_height = QLabel("Height (cm):")
        self.label_height.setStyleSheet("color: #333;")
        layout.addWidget(self.label_height, 1, 0)


        self.input_height = QLineEdit()
        self.input_height.setValidator(QDoubleValidator())
        self.input_height.setStyleSheet("color: black;")  # Черный текст
        layout.addWidget(self.input_height, 1, 1)


        self.button_calculate = QPushButton("Calculate")
        self.button_calculate.setStyleSheet("background-color: #4CAF50; color: white;")
        self.button_calculate.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.button_calculate, 2, 0, 1, 2)  # Кнопка занимает две колонки

        self.label_result = QLabel("Your BMI:")
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        layout.addWidget(self.label_result, 3, 0, 1, 2)  # Результат занимает две колонки

        #Categories Label
        self.label_categories = QLabel("BMI Categories:")
        self.label_categories.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        layout.addWidget(self.label_categories, 4, 0, 1, 2)  # Заголовок занимает две колонки

        self.label_underweight = QLabel("Underweight: < 18.5")
        self.label_underweight.setStyleSheet("background-color: yellow; color: black; padding: 5px;")
        layout.addWidget(self.label_underweight, 5, 0)

        self.label_normal = QLabel("Normal weight: 18.5 - 24.9")
        self.label_normal.setStyleSheet("background-color: green; color: black; padding: 5px;")
        layout.addWidget(self.label_normal, 5, 1)

        self.label_overweight = QLabel("Overweight: 25 - 29.9")
        self.label_overweight.setStyleSheet("background-color: orange; color: black; padding: 5px;")
        layout.addWidget(self.label_overweight, 6, 0)

        self.label_obese = QLabel("Obese: ≥ 30")
        self.label_obese.setStyleSheet("background-color: red; color: black; padding: 5px;")
        layout.addWidget(self.label_obese, 6, 1)

    def calculate_bmi(self):
        try:
            weight = float(self.input_weight.text())
            height = float(self.input_height.text()) / 100
            bmi = weight / (height ** 2)
            self.label_result.setText(f"Your BMI: {bmi:.2f}")

            if bmi < 18.5:
                self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black; background-color: yellow;")
            elif 18.5 <= bmi < 25:
                self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black; background-color: green;")
            elif 25 <= bmi < 30:
                self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black; background-color: orange;")
            else:
                self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black; background-color: red;")
        except ValueError:
            self.label_result.setText("Invalid input! Enter numbers only.")
            self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black; background-color: red;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    app.exec()