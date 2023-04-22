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
#Loop sum begins count value at 0
sum = 0
#counter begins at a value of 0
surveyCount = 0
#Display instructions and retrieve user input for counter evaluation
surveyValue = eval(input("VCU library services is conducting a survey\n""Please rate your overall satisfaction with VCU library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
#OUTER LOOP while/if
#Set loop to terminate program with sentinal control value -999 and print summary or continue survey loop
while surveyValue != -999:
            #NESTED if/else loop
            #Set conditions for invalid or valid survey rating value in survey value loop
            #If: user input rating is of a value 0-4 the rating is averaged and counted, this satisfies the if condition 
            if surveyValue >= 0 and surveyValue < 5:
                        #user input is added/accumulated to be averaged
                        sum = sum + surveyValue
                        #the rating value condition is met and counter is adjusted
                        surveyCount = surveyCount + 1
                        #prompt user for rating input
                        surveyValue = eval(input("VCU library services is conducting a survey\n""Please rate your overall satisfaction with VCU library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
            #Else: user input rating is not of a value 0-4 the rating is not averaged and not counted, this satisfies the else condition of the nested loop
            else:
                        #surveyValue >4 or surveyValue <0 #This is not required
                        #display message notifying the user that an incorrect value has been entered
                        print("You have not entered a valid rating.\n""Please try again.")
                        #user input is not recorded to sum or counter
                        surveyCount = surveyCount + 0
                        #this repeats the survey loop which prompts user for rating input
                        surveyValue = eval(input("VCU library services is conducting a survey\n""Please rate your overall satisfaction with VCU library services by entering a number from 0 (unsatisfactory) to 4 (satisfactory)."))
#Average rating and participation counter printout if value of -999 is entered in the terminal
if surveyCount > 0:
            #average valid rating inputs by survey count total
            surveyValue = sum /surveyCount
            #print summary with two decimal format
            print("Satisfactory rating for VCU library services: ", "{:.2f}" .format(surveyValue))
            #print total valid participants ratings
            print("Successful survey takers:", surveyCount)

            
