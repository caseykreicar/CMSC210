#check if the year is a leap year
#take user input for evaluation
year = eval(input("Enter a Year: "))
#check if the user input year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)
#display results
print(year, "is a leap year?", isLeapYear)
      
