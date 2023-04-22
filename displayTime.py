#display time program
seconds = eval(input("Please enter a number to be converted into seconds:"))
minutes = seconds // 60
remainingSeconds = seconds % 60
print("Number of seconds:", seconds, "\nMinutes:", minutes, "\nRemaing seconds:", remainingSeconds, "\n")
secondsInDays = 60 * 60 * 24
secondsInHours = 60* 60
secondsInMinutes = 60
days = seconds // secondsInDays
hours = (seconds - (days * secondsInDays)) // secondsInHours
minutesEquationTwo = (seconds - (days * secondsInDays) - (hours * secondsInHours)) // secondsInMinutes
print("Days:", days, "\nHours:", hours, "\nMinutes:", minutesEquationTwo)
