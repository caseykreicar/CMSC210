#Random math quiz
#Import Random function
import random
#Counter for percentage of correct answers
sum = 0
numberOfCorrectAnswers = 0
#Generate two single digit integers
numberOne = random.randint(0,50)
numberTwo = random.randint(0,50)
#If the numberOne < numberTwo, swap them
if numberOne < numberTwo:
    numberOne, numberTwo = numberTwo, numberOne
#Prompt for student to answer math problem 1 --------------------------------------
print("Question #1")
answerOne = eval(input("What is "+ str(numberOne) + " + " + str(numberTwo) + " ? "))
#Check answerOne and display the result
if numberOne + numberTwo == answerOne:
    print("Correct")
    sum = sum + 1
else:
    print("Incorrect \n ", numberOne, '+', numberTwo, "=", numberOne + numberTwo)
numberThree = random.randint(0,50)
numberFour = random.randint(0,50)
#If the numberThree < numberFour, swap them
if numberThree < numberFour:
    numberThree, numberFour = numberFour, numberThree
#Prompt for student to answer math problem 2---------------------------------------
print("Question #2")
answerTwo = eval(input("What is "+ str(numberThree) + " - " + str(numberFour) + " ? "))
#Check answerTwo and display the result
if numberThree - numberFour == answerTwo:
    print("Correct")
    sum = sum + 1
else:
    print("Incorrect \n", numberThree, '-', numberFour, "=", numberThree - numberFour)
numberFive = random.randint(0,50)
numberSix = random.randint(0,50)
#If the numberFive < numberSix, swap them
if numberFive < numberSix:
    numberFive, numberSix = numberSix, numberFive
#Prompt for student to answer math problem 3---------------------------------------
print("Question #3")
answerThree = eval(input("What is "+ str(numberFive) + " + " + str(numberSix) + " ? "))
#Check answerThree and display the result
if numberFive + numberSix == answerThree:
    print("Correct")
    sum = sum +1
else:
    print("Incorrect \n", numberFive, '+', numberSix, "=", numberFive + numberSix)
numberSeven = random.randint(0,50)
numberEight = random.randint(0,50)
#If the numberSeven < numberEight, swap them
if numberSeven < numberEight:
    numberSeven, numberEight = numberEight, numberSeven
#Prompt for student to answer math problem 4---------------------------------------
print("Question #4")
answerFour = eval(input("What is "+ str(numberSeven) + " - " + str(numberEight) + " ? "))
#Check answerFour and display the result
if numberSeven - numberEight == answerFour:
    print("Correct")
    sum = sum +1
else:
    print("Incorrect \n", numberSeven, '-', numberEight, "=", numberSeven - numberEight)
numberNine = random.randint(0,12)
numberTen = random.randint(0,12)
#If the numberNine < numberTen, swap them
if numberNine < numberTen:
    numberNine, numberTen = numberTen, numberNine
#Prompt for student to answer math problem 5---------------------------------------
print("Question #5")
answerFive = eval(input("What is "+ str(numberNine) + " * " + str(numberTen) + " ? "))
#Check answerFive and display the result
if numberNine * numberTen == answerFive:
    print("Correct")
    sum = sum +1
else:
    print("Incorrect \n", numberNine, 'x', numberTen, "=", numberNine * numberTen)
totalOfScore = sum / 5
finalScore = totalOfScore * 100
print("Your score is ", finalScore, "% out of 100 %")
if finalScore >= 90.0:
    grade = "A"
elif finalScore >= 80.0:
        grade = "B"
elif finalScore >= 70.0:
        grade = "C"
elif finalScore >= 60.0:
        grade = "D"
else:
    finalScore < 60.0
    grade = "F"
print("Grade: ", grade)
