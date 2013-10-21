password="kevin"
guess=""
print "WELCOME TO THE KEVSMART ATM, ENJOY YOUR STAY!"
print ""
while (password!=guess):
    guess=raw_input("Enter the password: ")

print ""
print("Access Granted")
print ""


canaccount=100.00
usaccount=100.00

while True:
	print "Current value of Canadian account is $",canaccount
	print ""
	print "Current value of American account is $",usaccount 
	print ""
	print "1.Deposit"
	print "2.Withdraw"
	print "3.Transfer"
	print "4.Exit"
	print ""
	choice=input("Would you like to do today? ")
	
	if (choice==4):
		print ""
		print "Thanks for using KEVsmart Account Management, have a nice day!"
		print ""
		break

	if (choice==1):
		print ""
		print "1.Canadian"
		print "2.American"
		print ""
		choice1=input("What account would you like to use? ")
 
		if (choice1==1):
			print ""
			print "You have chosen the Canadian Account."
			print ""
			value=input("How much in Canadian Dollars do you want to deposit? ")
			canaccount=canaccount+value
			print ""
			print "You have deposited $",value
			print ""
		    
		    
		if (choice1==2):
			print ""
			print "You have chosen the American Account."
			print ""
			value=input("How much in Canadian Dollars do you want to deposit? ")
			usaccount=usaccount+value
			print ""
			print "You have deposited $",value
		    
		
	if (choice==3):
		print ""
		print "1.Canadian"
		print "2.American"
		print ""
		choice3=input("Which account would you like to transfer money into?")
		
		if (choice3==1):
			print ""
			value=input("How much money would you like to transfer into your Canadian Account?: ")
			usaccount=usaccount-value
			canaccount=canaccount+value*1.04
			print ""
			print "You have transfered $",value
			
				
		if (choice3==2):
			print ""
			value=input("How much money would you like to transfer into your American Account?: ")
			usaccount=usaccount+value*0.96
			canaccount=canaccount-value
			print ""
			print "You have transfered $",value
			print ""
			

	if (choice==2):
		print ""
		print "1.Canadian"
		print "2.American"
		print ""
		choice2=input("Which account would you like to withdraw money out of?")
            
		if (choice2==1):
			print ""
			print "You have chosen your Canadian account."
			print ""
			value=input("How much money would you like to withdraw from your account?: ")
			canaccount=canaccount-value
			print ""
			print "You have withdrawn $",value
			print ""
			

		if (choice2==2):
			print ""
			print"You have chosen your American account."
			print ""
			value=input("How money would you like to withdraw from your account?: ")
			usaccount=usaccount-value
			print ""
			print "You have withdrawn $",value
			print ""
