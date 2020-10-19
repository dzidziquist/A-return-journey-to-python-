'''Making a simple calculator.
modify it to make it into a scientific calculator'''

#get the numbers 
num1 = float(input('enter a number'))

#the operations 
'''x and y are the numbers inputed by  the user'''
#addition
def add(x,y):
	return x + y

#subtraction 
def subtract(x,y):
	return x - y

#division

def divide(x,y):
	return x/y 

def multiply(x,y):
	return x*y

#select operation
operation = input('enter operation')
num2 = float(input('enter number'))
#the results 

#if + then addition
if operation == '+':
	result = add(num1, num2)
	print(result)

#if - then subtraction
elif operation == '-':
	result = subtract(num1, num2)
	print(result)

#if / then division
elif operation == '/':
	if num2 == 0:
		print('undefined')
	else:
		result = divide(num1, num2)
		print(result)

#if / then multiplication 
elif operation == '*':
	result = multiply(num1, num2)
	print(result)

else:
	print('invalid')