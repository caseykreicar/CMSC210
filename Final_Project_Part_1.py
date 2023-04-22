####################################
#Casey Latimere Kreicar
#CMSC 210
#Prof. Palesis
#May 6th, 2021
####################################
#Final Project Part 1: High, Medium, and Low Positive Numbers
#50 points total
#
#Problem Description:
#Write a python program that creates a list of positive numbers entered by the user
#one at a time from the keyboard and processes this list to count how many
#numbers are high (100 or greater), how many numbers are medium (50 or greater
#and less than 100) and how many numbers are low (0 or greater and less than 50).
#
#The Solution:
#
#Create an empty list: 2 points
#Create an empty list in the blank line below for storing the numbers that
#will be entered by the user.  Give it a good descriptive name.
######################START######################################
listArray = []
lowNumberCount = 0
mediumNumberCount = 0
highNumberCount = 0
totalNumbersInList = int(input("Enter the total number of items you wish to input into your list\n"))
print("\nInstructions:\nPlease enter one positive number at a time pressing enter after each entry, until a printout of your populated list is generated\n")
for i in range(totalNumbersInList):
      inputData = int(input("Enter the number here and press enter: "))
      listArray.append("%.2f" % inputData)
      if  inputData < 50:
            lowNumberCount = lowNumberCount + 1
      elif inputData > 49 and inputData <100:
            mediumNumberCount = mediumNumberCount + 1
      else:
            inputData > 99
            highNumberCount = highNumberCount + 1
print("\nYour list consists of the following numbers: ", listArray)
print("\nYour list has been processed/categorized into the following three fields below:\n\n Low numbers | representing less than 50 \n Medium numbers | representing greater than or equal to 50 and less than 100 \n High numbers | representing greater than 100")
print("\nYour results:\n Low number count: ", lowNumberCount, "\n Medium number count: ", mediumNumberCount, "\n High number count: ", highNumberCount)
#####################END##########################################
#Populate the list using a while loop: 20 points
#Create a while loop that populates the list of numbers by prompting the user
#to enter one number at a time. The number entry stops when the user enters -1.
#Assume the user enters the correct type of data, i.e., a positive number or -1.
#Covert the numbers entered by the user to floating point.
#Using the append() list method, add each positive number entered to the list.
#Hint 1: Do not forget to add any initialization staements needed before the loop.
#Hint 2: Do not forget to include inside your loop the statement(s) that will 
#eventually cause the loop to stop.
#Use as many lines of code as needed.
#
#Print the list: 2 points
#Write a simple print statement to print your list.
#Include a brief user-friendly wording in your print statement to explain what is being printed.
#
#Process the list using a for loop: 20 points
#Using a for loop, process the created number list as follows:
#count how many numbers are high (100 or higher)
#how many numbers are medium (50 or highter but less than 100)
#and how many numbers are low (0 or higher and less than 50).
#Hint 1: Do not forget to initialize the various counts before your for loop starts
#Hint 2: the body of your for loop should be a decision block.
#Use as many lines of code as needed.
#
#Output the results: 6 points
#Output a user-friendly report of the results of the list processing
#using one or more print statements
#
#################EXPERIMENTAL CODE######################
######################################################
#FOR
#listArray = []
#numbersInList = int(input("Enter total number items in the list"))
#print("Enter Numbers")
#for i in range(numbersInList):
#      data=int(input())
#      listArray.append(data)
#print(listArray)
###############################################
###################################
#WHILE LOOP
#couldn't figure out how to get user input into an array(list) and in a WHILE loop using previous project examples
#sum = 0
#listCount = 0
#lowNumbers = 0
#mediumNumbers = 0
#highNumbers = 0
#listPopulation = eval(input("Please enter a positive number: "))
#while listPopulation != -1:
#            if listPopulation >0:
#                        sum = sum + listPopulation
#                        listCount = listCount + 1
#                        listPopulation = eval(input("Please enter a positive number: "))
#            else:
#                        print("Invalid entry, zero is not a positive number")
#                        listCount = listCount + 0
#                        listPopulation = eval(input("Please enter a positive number: "))
#if listCount > 0:
#            listAverage = sum/listCount
#            print("Mean: ", "{:.2f}" .format(listAverage))
#            print("Total items: ", listCount)
######################################################
#sum = 0
#listInput = ""
#while listnInput != -1:
#           listInput = input("Enter your list of numbers seperated by a comma and space ie... 3, 5, 6, 2 and press enter.\n")
#            print(type(listInput.split(", ")))
#            print(listInput.split(", "))
#if listInput > 0:
#            print(listInput.split(", "))
######################################################
######################################################
