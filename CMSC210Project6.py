#######################
#Casey Latimere Kreicar 
#CMSC 210 Python Project 6 
#Prof. Palesis 
#April 5th 2021 
#######################
#
#For Loop Assignment
#
###START###
#
#Array/List
numList = [6,3,9,4,7]
#Declare/Initialize current max number within list
maxNum = 0
#For loop statement, if a higher number is added to the numList array, maxNum equals new highest number in the array and is printed
for N in numList:
    if N > maxNum: maxNum = N
print("Highest Value within the list: ", maxNum)
#
###END###
