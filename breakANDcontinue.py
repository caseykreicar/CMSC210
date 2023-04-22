#break and continue statements

#break
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number, "\nNumber of values entered is", counter)
else:
    print("You haven't entered any number.")


#continue
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number, "\nNumber of values entered is", counter)
else:
    print("You haven't entered any number.")

#practice scenario MY ATTEMPT

#chupacabra = True

#while True:
  #          userInput = input("Enter a word")
    #        if userInput == chupacabra:
      #                  break
        #    if userInput != chupacabra:
          #              userInput = input("Enter a word")
            #else:
              #          print("You haven't entered a word")

#Found on the internet
secret_word = ""
while True:
    secret_word = input("You're stuck in an infinite loop!\nEnter a secret word to leave the loop.")
    if secret_word == "chupacabra":
        print("You've successfully left the loop.")
        break

