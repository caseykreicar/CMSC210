#######################
#Casey Latimere Kreicar 
#CMSC 210 Python Project 3 Counting Dollars
#Prof. Palesis 
#March 3rd 2021 
#######################
#
#############START#############
#Display message from your friendly financial facility
print("Welcome to Casey's Coin Counting Services!")
#############QUARTERS##########
#Display message prompting user to enter the amount of Quarters
print("Please enter the total number of Quarters you would like to be counted")
#User Input
numQuarters = input("Enter a number: ")
#Display amount of quarters entered by user
print("Quantity of quarters entered by user:", numQuarters)
#Convert user input into value that can be calculated
numQuarters = int(numQuarters)
#Calculate user input/quantity of quarters into dollar value
totalValueOfQuarters = numQuarters * .25
twoDecimalFormatQuarters ="{:.2f}" .format(totalValueOfQuarters)
print("Total dollar amount of Quarters in $USD:", twoDecimalFormatQuarters)
#Final calculation value
quartersFinalAmount = float(twoDecimalFormatQuarters)
#############DIMES#############
#Display message prompting user to enter the amount of Dimes
print("Please enter the total number of Dimes you would like to be counted")
#User Input
numDimes = input("Enter a number: ")
#Display amount of quarters entered by user
print("Quantity of dimes entered by user:", numDimes)
#Convert user input into value that can be calculated
numDimes = int(numDimes)
#Calculate user input/quantity of Dimes into dollar value
totalValueOfDimes = numDimes * .10
twoDecimalFormatDimes ="{:.2f}" .format(totalValueOfDimes)
print("Total dollar amount of Quarters in $USD:", twoDecimalFormatDimes)
#Final calculation value
dimesFinalAmount = float(twoDecimalFormatDimes)
#############NICKELS############
#Display message prompting user to enter the amount of Nickels
print("Please enter the total number of Nickels you would like to be counted")
#User Input
numNickels = input("Enter a number: ")
#Display amount of nickels entered by user
print("Quantity of nickels entered by user:", numNickels)
#Convert user input into value that can be calculated
numNickels = int(numNickels)
#Calculate user input/quantity of Nickels into dollar value
totalValueOfNickels = numNickels * .05
twoDecimalFormatNickels ="{:.2f}" .format(totalValueOfNickels)
print("Total dollar amount of Nickels in $USD:", twoDecimalFormatNickels)
#Final calculation value
nickelsFinalAmount = float(twoDecimalFormatNickels)
#############PENNIES#############
#Display message prompting user to enter the amount of Pennies
print("Please enter the total number of Pennies you would like to be counted")
#User Input
numPennies = input("Enter a number: ")
#Display amount of nickels entered by user
print("Quantity of pennies entered by user:", numPennies)
#Convert user input into value that can be calculated
numPennies = int(numPennies)
#Calculate user input/quantity of Pennies into dollar value
totalValueOfPennies = numPennies * .01
twoDecimalFormatPennies ="{:.2f}" .format(totalValueOfPennies)
print("Total dollar amount of Pennies in $USD:", twoDecimalFormatPennies)
#Final calculation value
penniesFinalAmount = float(twoDecimalFormatPennies)
##############TOTAL##############
totalDollarAmount = sum([quartersFinalAmount, dimesFinalAmount, nickelsFinalAmount, penniesFinalAmount])
totalAmountDecimal ="{:.2f}" .format(totalDollarAmount)
print("Total Amount in $USD:", totalAmountDecimal)
#
############END#################
