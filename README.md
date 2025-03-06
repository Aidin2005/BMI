# BMI Calculator

## Objective: Create a BMI Calculator application using PyQt  that allows users to calculate their Body Mass Index (BMI) and provides information on their BMI status according to the Department of Health and Human Services/National Institutes of Health guidelines.
Instructions:
## 1. User Interface:
Design a PyQt user interface for the BMI calculator.
The user interface should include the following components:
QLabel and QLineEdit for weight and height input.
A "Calculate BMI" button.
A Label to display the BMI result.
Display BMI status (Underweight, Normal, Overweight, Obese) based on the calculated BMI.
## 2. BMI Calculation:
Implement the BMI calculation based on user input.
Display the calculated BMI in the designated area in the user interface.
The formula for calculating the BMI = Weight(kg)/[Height(m)]2


# BMI Calculator

A simple BMI (Body Mass Index) calculator built with PyQt6.

## Installation

Ensure you have Python installed, then install the required dependencies:

```sh
pip install PyQt6
```

## Usage

Run the script:

```sh
python bmi_calculator.py
```

## Sample Input and Output

### Input:
```plaintext
Weight: 70 kg
Height: 175 cm
```
<img width="531" alt="Screenshot 2025-03-06 at 11 00 35 PM" src="https://github.com/user-attachments/assets/cf60442b-c977-40bb-a779-7b08817c61af" />

### Output:
```plaintext
Your BMI: 22.86
Category: Normal
```
<img width="537" alt="Screenshot 2025-03-06 at 11 01 34 PM" src="https://github.com/user-attachments/assets/27aa9247-62c6-47f5-9085-45310bdde401" />


### BMI Categories:

```plaintext
Underweight: <18.5 (Yellow)
Normal: 18.5 - 24.9 (Green)
Overweight: 25 - 29.9 (Orange)
Obese: >=30 (Red)
```

## Features
- User-friendly PyQt6 interface
- Color-coded BMI category display
- Input validation for weight and height


