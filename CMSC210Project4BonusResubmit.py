#######################
#Casey Latimere Kreicar 
#CMSC 210 Python Project 4 End of Year Bonus
#Prof. Palesis 
#March 25th 2021 
#######################
#
#
#############START#############
#
####USER INFORMATION####
#Display instructions for user to begin the process of determining their end of year bonus
print("To determine your end of year bonus, please enter the following information when prompted:")
print("NOTE: Your bonus is calculated under the following guidelines, the qualifying bracket represents the value being implemented")
print("Average monthly sales amount: less than $1,000 = $100 | less $2,000 = $200 | less than $3,000 = $3,000 | and $3,000 or more = $400")
print("Adjusted based on years of employment: less than 10 years = no adjustment | less than 20 years = 10% increase | 20 years or more = 20%")
#Retrieve User First Name Input
usrFirstName = input("Please enter your first name: ")      
#Retrieve User Last Name Input
usrLastName = input("Please enter your last name: ")
#Retrieve User number of years with company
usrYearsWithCompany = int(input("Please enter your number of years with the company: "))
####DECISION STATEMENTS####
#Statement to determine bonus increase based by years
if usrYearsWithCompany <10:
            bonusAdjustment = 0
elif usrYearsWithCompany <20:
            bonusAdjustment = .10
            print("Note: Bonus will be adjusted by 10%")
else:
            bonusAdjustment = .20
            print("Note: Bonus will be adjusted by 20%")
#
#test adjustment value
#print(bonusAdjustment)
#Retrieve User number of sales
usrSalesNumber = int(input("Please enter your number of sales this year: "))
#Statement to determine bonus amount based on sales
if usrSalesNumber <1000:
            bonusAmount = 100
elif usrSalesNumber <2000:
            bonusAmount = 200
elif usrSalesNumber <3000:
            bonusAmount = 300
else:
            bonusAmount = 400
#
#test adjustment value
#print(bonusAmount)
####CALCULATION####
bonusTotal = sum([bonusAdjustment * bonusAmount + bonusAmount])
bonusTotalAmount ="{:.2f}" .format(bonusTotal)
print("___________________________________________________________")
print("Salesperson: ", usrFirstName, usrLastName)
print("Number of years with the company: ", usrYearsWithCompany)
print("Total Sales: $", usrSalesNumber)
print("Bonus Amount:  $", bonusTotalAmount)
#
#
#
#
#############END##############
#
#
#
#
####ABANDONED DECISION STATEMENT####
#Statement Structure for determining adjusted bonus percentage based on years at company and sales number
#
#Wasn't able to figure this out with nested statements
#
#if usrYearsWithCompany: >=10 and <=19
#adjustedBonus = .10
#           if usrTotalSales <= 1000:
#                       bonus = (adjustedBonus * 100 +100)
#            elif usrTotalSales >= 2000 and <= 2999:
#                       bonus = (adjustedBonus * 200 + 200)
#            else
#                       usrTotalSales > 3000
#elif usrYearsWithCompany >=20
#adjustedBonus = .20
#           if usrTotalSales <= 1000:
#                       bonus = (adjustedBonus * 100 +100)
#          elif usrTotalSales >= 2000 and <= 2999:
#                       bonus = (adjustedBonus * 200 + 200)
#          else:
#                     usrTotalSales > 3000     
#else:
#           if usrTotalSales <= 1000:
#                       bonus = 100
#           elif usrTotalSales >= 2000 and <= 2999:
#                       bonus = 200
#           else:
#                      usrTotalSales > 3000
#                      bonus = 300






