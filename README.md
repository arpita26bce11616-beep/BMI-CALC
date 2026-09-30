BMI Calculator

A simple and interactive BMI Calculator developed in Python. This project takes basic user information as input, calculates Body Mass Index (BMI), displays the result, and classifies the entered age into an age group.

The project was created as part of a Python Essentials Project to demonstrate the practical use of fundamental Python programming concepts.

About the Project

The BMI Calculator allows the user to enter their:

Name
Age
Gender
Height in centimetres
Weight in kilograms

The program converts the height from centimetres to metres and calculates BMI using the standard mathematical formula. The calculated value is rounded to two decimal places and displayed along with the category implemented in the program.

The program also identifies the user's age group and provides a simple option to perform another calculation without restarting the program.

Features
Interactive user input
BMI calculation from height and weight
BMI value rounded to two decimal places
BMI category display
Age-group classification
Basic input validation for height and weight
Option to calculate BMI multiple times
Clear and organized console output
Uses separate functions for different parts of the program
How the Program Works

The program is organized into three main functions:

get_details()

Collects the user's name, age, gender, height, and weight and returns these values to the main program.

calculate_bmi(height, weight)

Converts height from centimetres to metres and calculates BMI using:

BMI = Weight / (Height × Height)

The result is rounded to two decimal places.

show_result(...)

Displays the user's details, calculated BMI, BMI category, age group, and the corresponding messages defined in the program.

Python Concepts Used

This project demonstrates several fundamental Python concepts:

Functions
Variables
User input
Data type conversion
Arithmetic operations
if, elif, and else statements
while loops
break statement
String methods
Comparison operators
Basic input validation
Returning values from functions
Program Flow
The program displays a welcome message.
The user enters their personal details.
Height and weight are checked to ensure they are greater than zero.
Height is converted from centimetres to metres.
BMI is calculated and rounded to two decimal places.
The BMI result and category are displayed.
The user's age group is displayed.
The user can choose to perform another calculation.
The program ends when the user selects no or enters an invalid choice.
Requirements

To run this project, you only need:

Python 3.x
A Python-compatible editor or IDE, such as VS Code

No external libraries are required.

How to Run
Make sure Python 3.x is installed on your computer.
Download or clone this repository.
Open the project in your preferred Python editor.
Run the Python file.
Follow the instructions displayed in the terminal.
Project Structure
BMI-Calculator/
│
├── Project 5 Python.py
└── README.md
Purpose

The main purpose of this project is to apply basic Python programming concepts to create a functional, interactive program. It demonstrates how functions, calculations, conditional logic, loops, and user input can be combined to build a simple real-world application.

Note

This project is intended for educational purposes and demonstrates BMI calculation and categorization as implemented in the program. BMI is a screening measure and does not provide a complete assessment of an individual's health.

Python Essentials Project
Developed by: Arpita Mittal
