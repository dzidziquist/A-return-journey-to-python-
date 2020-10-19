'''identifying the operations of scientific :
trig functions 
log functions 
ceiling floor 
factorial
exponential 

'''
import math as m

num1 = float(input('enter a number'))


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
#the results 

#if + then addition
if operation == '+':
	num2 = float(input('enter number'))
	result = add(num1, num2)
	print(result)

#if - then subtraction
elif operation == '-':
	num2 = float(input('enter number'))
	result = subtract(num1, num2)
	print(result)

#if / then division
elif operation == '/':
	num2 = float(input('enter number'))
	if num2 == 0:
		print('undefined')
	else:
		result = divide(num1, num2)
		print(result)

#if / then multiplication 
elif operation == '*':
	num2 = float(input('enter number'))
	result = multiply(num1, num2)
	print(result)

#ceiling 
elif operation =='ceil':
	result = m.ceil(num1)
	print(result)

#floor
elif operation == 'floor':
	result = m.floor(num1)
	print(result)

#factorial 
elif operation == '!':
	result = m.factorial(num1)
	print(result)

#exponentail 
elif operation == 'exp':
	result = m.exp(num1)
	print(result)

#log 

elif operation == 'log':
	result = m.log(num1)
	print(result)

elif operation == 'log10':
	result = m.log10(num1)
	print(result)

elif operation == 'log2':
	result = m.log10(num1)
	print(result)

#square root 
elif operation == 'sqrt':
	result = m.sqrt(num1)
	print(result) 

#trig functions
#cosine
elif operation == 'cos':
	result = m.cos(num1)
	print(result) 

#sine
elif operation == 'sin':
	result = m.sin(num1)
	print(result) 

#tan
elif operation == 'tan':
	result = m.tan(num1)
	print(result) 

#angular conversion
elif operation == 'degrees':
	result = m.degrees(num1)
	print(result)

elif operation == 'rad':
	result = m.radians(num1)
	print(result)  

else:
	print('invalid')