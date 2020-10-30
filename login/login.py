'''Creating a basic script to accept username and password'''

#importing the saved user information 
from user_info import username, password, secret_code

#let's try to loop till the user gets the login correct 
count = 0

#after 3 tries block account 
while count < 4:
	#allow user to enter username 
	userinput1 = input('enter your username')
	userinput2 = input('enter your password')

	#checking for correctness 

	if userinput1 == username and userinput2 == password:
		print('Hello there!, Welcome to your account')
		break 
	else:
		print('Wrong user or invalid password. Try again\n', 'reset account details')
		userinput3 = input('try again or reset')
		if userinput3 == 'reset':
			userinput4 = input('enter your secret code used for registration')
			if secret_code == userinput4:
				userinput5 = input('enter new username')
				userinput6 = input('enter new password')
				print('Hello there!, Welcome to your account')
				break

		else: 
			count += 1
			if count > 3:
				print('too many tries, account has been blocked')


		

