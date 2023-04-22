#Guess the secret number to escape the loop
secretNumber = 7
print(
"""
+================================+
| Welcome to my game, muggle!               |
| Enter an integer number                           |
| and guess what number I've                     |
| picked for you.                                            |
| So, what is the secret number?                |
+================================+
""")

usersGuessNumber = int(input("Please enter a number from 1-10 and press enter until you have found the secret number: "))
while usersGuessNumber != 7:
            print("Sorry you have not found the secret number, please try again!")
            usersGuessNumber = int(input("Please enter a number from 1-10 and press enter until you have found the secret number: "))
print("Congratulations! You found the secret number.")

