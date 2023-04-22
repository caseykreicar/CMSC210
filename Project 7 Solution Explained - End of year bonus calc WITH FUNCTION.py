#Project 7 Solution Explained: End of Year Bonus Calculation WITH A FUNCTION
#
#Function definition:
#Our function uses yearly sales and years of service to calculate the employee bonus.
#Thus, it must have two parameters: one for yearly sales and one for years of service.  
#Note that in the function header below, we chose to use parameter names for yearly sales
#and years of service that are different from the equivalent variable names used in
#the original program. Using the same names would also work but it is better to use
#different names to emphasize that the names we give the parameters do not really matter.
#A good descriptive name for our function itself is 'bonusCalc'.
#Here is the header (i.e., the signature):
def bonusCalc(sales,service):
    #Now, we must move ALL the code for calculating the bonus inside the function.
    #Of course, we have to properly INDENT the code
    #and change the original variable names for yearly sales ('yearSales') and years of service
    #('yearsOfService') to the parameter names which are: 'sales' and 'service'.
    #The rest of the variable names can remain the same.
    #First, we calculate the sales monthly average:
    monthlyAve = sales/12  #Note that here we are using the parameter name: 'sales'
    #Now we calculate the bonus as before.
    #The code for calculating the bonus does not need to change at all.
    #Decide bonus
    if monthlyAve < 1000:
        bonus = 100
    elif monthlyAve >= 1000 and monthlyAve < 2000:
        bonus = 200
    elif monthlyAve >= 2000 and monthlyAve < 3000:
        bonus = 300
    else: 
        bonus = 400
    #
    #Adjust bonus per years of service
    if yearsOfService >= 20:
        finalBonus = bonus*1.20
    elif yearsOfService >= 10:
        finalBonus =  bonus*1.10
    else:
        finalBonus = bonus
    #
    #Now that the final bonus ('finalBonus') has been calculated, all we need to do is to return
    #its value to the calling program:
    return finalBonus
    #...and the function ends here.
#
#
#Here is the main program which prompts the user to input
#the basic data: yearly sales and years of service
yearSales=float(input("Enter the total sales for the year: "))
yearsOfService = int(input("Enter the number of years with the company: "))
#
#Next, the main program calls the function using as arguments the data
#inputed by the user.  Note that we must make sure the order of the arguments
#matches the order of the function parameters which will receive the argument values:
#the function parameter 'sales' must receive the value of 'yearSales' and
#the function parameter 'service' must receive the value of 'yearsOfService'.
#When the function executes, it returns the final bonus calculated for those inputs.
#We can store the value returned by the function into a new variable
#here and then print it.
calculatedBonus = bonusCalc(yearSales,yearsOfService)
print("The bonus for the year is {0:.2f}.".format(calculatedBonus))
#That's all folks!!!
