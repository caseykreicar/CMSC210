#ComputeLoan Program
annualInterestRate = eval(input("Enter annual interest rate: "))
#Calculate Interest Rate
monthlyInterestRate = annualInterestRate / 1200
#Enter Number of Years
numberOfYears = eval(input("Enter number of years: "))
#Enter Loan Amount
loanAmount = eval(input("Enter loan amount: "))
#Calculate Payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment =  monthlyPayment * numberOfYears * 12
#Display Results
print("The monthly Payment is: ", int(monthlyPayment * 100) / 100)
print("The total Payment is: ", int(totalPayment * 100) / 100) 
