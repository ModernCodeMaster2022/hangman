import random
import tkinter

words = ["space","rocket","submarines","deepsea","geographers","moon","sonar","magnetometers","satellites","buoys","rovers","compasses","lens","astronauts"]
word = random.choice(words)
guesses = 6
user_guess = ''
allowed_letters = set('abcdefghijklmnopqrstuvwxyz')
while len(word) > 0:
    character_guess = ""
    wrong = 0

    for letter in word:
        if letter in user_guess:
            character_guess = character_guess+letter
        else:
            character_guess = character_guess+"_ "

    if character_guess == word:
        print("You successfully uncovered the word!!")
        print(word+"!")
        break

    print("Guess the words",character_guess)
    user1 = input()

    if user1 in allowed_letters:
        user_guess = user_guess+user1
    else:
        user1 = input("Enter a letter ONLY.")
        user1=input()

    if user1 not in word:
        guesses = guesses-1

        if guesses==5:
            print("Incorrect! You have 5 more tries!")
            print("---------------------------------")
            print("              |__O               ")
            print("              |                  ")
            print("              |                  ")
            print("              |_____             ")
        if guesses==4:
            print("Incorrect! You have 4 more tries!")
            print("---------------------------------")
            print("             |__O                ")
            print("             |  |                ")
            print("             |                   ")
            print("             |_____              ")
        if guesses==3:
            print("Incorrect! You have 3 more tries!")
            print("---------------------------------")
            print("             |__O                ")
            print("             | \|                ")
            print("             |                   ")
            print("             |_____              ")
        if guesses==2:
            print("Incorrect! You have 2 more tries!")
            print("---------------------------------")
            print("             |__O                ")
            print("             | \|/               ")
            print("             |                   ")
            print("             |_____              ")
        if guesses==1:
            print("Last try, be careful!")
            print("---------------------------------")
            print("             |__O                ")
            print("             | \|/               ")
            print("             | /                 ")
            print("             |_____              ")
        if guesses==0:
            print("Oh no, you ran out of tries! Game over! :(")
            print("---------------------------------")
            print("             |__O                ")
            print("             | \|/               ")
            print("             | / \               ")
            print("             |_____              ")
            print("The word was",word)
            break