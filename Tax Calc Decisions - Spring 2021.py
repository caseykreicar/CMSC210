'''
Python Decisions Example
CMSC 210, Spring 2021
Dr. John A. Palesis

This program Calculates the income taxes owed based on the filing status
(Single or Married Filing Jointly) and the income.

The following table is used for the tax decision:

Tax Rate     Single Income         Married Filing Jointly Income
0%           Up to $30,400         Up to $60,800
12%          $30,401 - $84,200     $60,801 - $168,400 
24%          $84,201 - $160,725    $168,401 - $321,450 
35%          Over $160,726         Over $321,451
'''
#
#Prompt the user to enter the tax status.
#To make user input easier and more reliable,the user is prompted
#to enter 1 for filing single and 2 for filing Married Filing Jointly.
#We convert user input for taxStatus to an integer.
taxStatus = int(input("Tax status - enter 1 for Single or 2 for Married Filing Jointly: "))
#Make sure user input is correct before proceeding to the tax decision.
#We terminate program execution if user input is not 1 or 2.
if taxStatus != 1 and taxStatus != 2:
    quit("Input error.  Start the program again.")
#We continue normal processing here only if user input is 1 or 2.
#
#Promput user to enter the income which we convert to a float.
income = float(input("Enter your income:"))
#
#Now we build the tax decision logic.
#
#To make this logic more meaningful and easier to follow
#we will use two Boolean variables to represent taxStatus:
#singleFiling and marriedFilingJointly.
#If user entered 1 above, singleFiling is set to True
#and marriedFilingJointly is set to False.
#Conversely,if user entered a 2 for filing status, singleFiling is set to False
#and marriedFilingJointly is set to True.
#Remember that taxStatuse is guaranteed to be 1 or 2 at this point so we do not need
#to consider any other conditions.
if taxStatus == 1:
    singleFiling = True
    marriedFilingJointly = False
else:
    singleFiling = False
    marriedFilingJointly = True
#So, at this point, only one of the two can be true: singleFiling or marriedFilingJointly.
#
#Implementing the tax percent decision using a nested if statement:
#There are multiple ways to implement the decision logic.
#The tax percent decision must be established first based on filing status
#and then based on income ranges which are different for each filing status.
#Thus, the most intuitive algorithm for this decision problem is the nested if-statement structue.
#Here is the nested-if decision logic:
if singleFiling:
    if income <= 30400:
        taxRate=0
    elif income <= 84200:
        taxRate = 12
    elif income <= 160725:
        taxRate = 24
    else:
        taxRate = 35
else:
    if income <= 60800:
        taxRate=0
    elif income <= 168400:
        taxRate = 12
    elif income <= 321450:
        taxRate = 24
    else:
        taxRate = 35
#
#Now we can calculate the actual taxes owed using established tax rate percent and the income:
taxAmount = income*taxRate/100
#
#Finally, we can output the results:
#Filing status:
if singleFiling == True:
    print("Your filing status is Single.")
else:
    print("Your filing status is Married Filing Jointly.") 
#Income:
#Note the use of comma below within the brackets.  It serves to format the number printed
#using commas if the number is a thousand or more.
print('Your reported income is: ${0:,.2f}'.format(income))
#Tax Rate:
#Format Tax Rate Percent as a real number with two decimals.
print('Tax Rate used: {0:.2f}%'.format(taxRate))
#Taxes owed:
print('Your tax amount is: ${0:,.2f}'.format(taxAmount))
