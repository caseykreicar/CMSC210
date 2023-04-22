######################
#Casey Latimere Kreicar
#CMSC 210
#Prof. Palesis
#May 6th 2021
######################
#Final Project Part 2
#Create and use a simple python function
#50 points total
#
#The problem:
#You will create a function that receives as input two different strings:
#one for the first name and one for the last name of a user.
#The function will convert both the first and last names to upper case
#and then use these upper case strings to build a new string for the
#user full name with this format:
#LAST_NAME, FIRST_NAME (a coma and a space must be added after the last name).
#For example, if the inputs to the function are 'John' for first name and
#'Doe' for last name, the full name string returned by the function should be:
#DOE, JOHN
#In your main program, you must include the code that prompts the user
#to enter a fist name and a last name and then calls the function to convert them
#to the proper format. 
#
#The solution:
#
################START###########################
#
#Create the function header: 15 points
#
########FUNCTION#####
def functionCode():
            lastNameString = lastName
            lastNameStringUpper = lastNameString.upper()
            firstNameString = firstName
            firstNameStringUpper = firstNameString.upper()
            fullNameFormat = lastNameStringUpper, firstNameStringUpper
            print(fullNameFormat)
            return
#Give your function a good descriptive name.
#The parameter names you use must be different from
#the variable names you will use in the main program.
    #
    #Convert the parameter values to upper case: 6 points
    #Hint: Use a string object method
    #
    #Create and return the full name string with proper format: 8 points
    #Remember: the full name format is: LAST_NAME, FIRST_NAME
    #You may use one or two statements below:
    #Your function ends here.
#
######MAIN########
#
#Name entry: 6 points
#Prompt user to enter a first name and then a last name
#and store the inputed strings using two new variable names
#(not the same names used for function parameters).
#You can assume that the user enters the data correctly
#(in other words, you do not need to check for any improper user input).
#Insert your two lines of code below:
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
#Call the function and print the returned full name: 15 points
#Call your function to construct the full name for the firs and last
#names entered by the user and print the formatted full name retured
#by the function.
functionCode()
#################END##############
#
#Hint: you can store the full name returned by the function in a new variable
#and then print out that variable value.



