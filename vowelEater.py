#for loop vowel eater

#define this variable for later print out the word without vowels
wordWithoutVowels = ""
#define the variable based on user input
userWord = input("Please Enter a word: ")
#append variable to all upper case letters with the .upper () function
userWord = userWord.upper()
#for loop using the letter variable in range of the string
for letter in userWord:
#if letter A is present it will remove it? #if the values of the two operands are equal, then the condition becomes true
    if letter == 'A':
        word = letter
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
            #if the value 
            wordWithoutVowels+=letter
for index, letter in enumerate(wordWithoutVowels,1):
            print(letter)
                


