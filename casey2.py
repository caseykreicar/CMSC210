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
#Loop sum begins count at 0
sum = 0
surveyCount = 0
#Display instructions and retrieve user input
surveyValue = eval(input("Please rate your overall satisfaction with VCU Library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
#Set conditions for loop
while surveyValue != -999:
            if surveyValue >= 0 and surveyValue < 5:  ###better to us <= 4
                        sum = sum + surveyValue
                        surveyCount = surveyCount + 1
                        ###the line below must be after the if-else condition
                        surveyValue = eval(input("Please rate your overall satisfaction with VCU Library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
            else:
                        surveyValue >4 or surveyValue <0 ###remove this line
                        print("You have not entered a valid rating value")
            ###here is where you put the input statement to get the next rating.

if surveyCount > 0:
            surveyValue = sum /surveyCount
            print("Average Satisfaction Rating for VCU Library services: ", "{:.2f}" .format(surveyValue))
            print("Survey Takers:", surveyCount)

            
