#Casey Latimere Kreicar
#CMSC 210 Project 7 Function w/Bonus Program
#Prof. Palesis
#April 19th 2021
#
#
#
######START######
#
##FUNCTION## 
#
#Define function
def totalBonusFunction():
#Calculate the total bonus by adjusting the sales bonus
#per years of service:
#if years of service is 10 or more,
#increase the sales bonus by the appropriate percent
            if yearsOfService >= 20:
                        totalBonus = salesBonus*1.20
            elif yearsOfService >= 10:
                        totalBonus =  salesBonus*1.10
            else:
                        totalBonus = salesBonus
            print("The bonus for the year is {0:.2f}.".format(totalBonus))
#
#
#
#
######MAIN PROGRAM######
#
#End of Year Bonus Calculation
#
#Enter basic data
yearSales=float(input("Enter the total sales for the year: "))
yearsOfService = int(input("Enter the number of years with the company: "))
#
#Calculate monthly sales
monthlyAveSales = yearSales/12
#
#Decide sales bonus based on monthly sales average
if monthlyAveSales < 1000:
    salesBonus = 100
elif monthlyAveSales >= 1000 and monthlyAveSales < 2000:
    salesBonus = 200
elif monthlyAveSales >= 2000 and monthlyAveSales < 3000:
    salesBonus = 300
else: 
    salesBonus = 400
#
#
#Call Function
totalBonusFunction()
#
#
######END######
