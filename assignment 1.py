##Task 1: Perform Basic Mathematical Operations
"""
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
	Addition
	Subtraction
	Multiplication
	Division
3.  Displays the results of each operation on the screen.
"""

#RESULTS
num1 = (int(input('enter first number:')))
num2 = (int(input('enter second number:')))
Addition =(num1 + num2)
Substraction =(num2 - num1)
Multiplication =(num1 * num2)
Division =(num1 // num2)
print('Addition =', Addition)
print('Subtraction =', Substraction)
print('Multiplication =', Multiplication)
print('Division =', Division)

## TASK 2 - Creating a personalised greeting
first_name = input('enter your first name:')
last_name = input('enter your last name:')
full_name = (first_name + last_name )
print('hello', full_name ,'welcome to the python program')