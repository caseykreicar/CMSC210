#####################
#Casey Latimere Kreicar
#CMSC 210 Python Project 5 VCU Library Survey
#Prof. Palesis
#March 31st, 2021
#####################
#
#
#
#######START#########
#
#Loops sum begins count at 0
sum = 0
surveyCount = 0
#Display instructions and retrieve user input
surveyValue = eval(input("Please rate your overall satisfaction with VCU Library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
#Set conditions for loop
while surveyValue != -999:
            ###Here you should have an if statement to assure the input is valid before you include it in the survey, else (if not valid, you simply inform the user that the input is invalid
            sum = sum + surveyValue
            surveyCount = surveyCount + 1
            surveyValue = eval(input("Please rate your overall satisfaction with VCU Library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
if surveyCount > 0:
            surveyValue = sum /surveyCount
            print("Average Satisfaction Rating for VCU Library services: ", "{:.2f}" .format(surveyValue))
            print("Survey Takers:", surveyCount)
else:
            ###This code belongs in the while loop since it needs to be used every time an invalid input is used.
            surveyValue > 5  ###Is this an if statement?  Needs an 'if'. But note also that an invalid rating can also be a negative number...
            print("You have not entered a valid rating")
            
