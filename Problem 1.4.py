def hangaroo(secretWord):
    length=len(secretWord)
    print("Welcome to the game Hangaroo!")
    print("My word is", length, "letters long.")
    chances=4
    i=0
    lettersGuessed=[]
    while (chances!=0):
        print("------------")
        if secretWord!= getGuessedWord(secretWord,lettersGuessed):
            print("You have", chances, "guesses left.")
            print("Available letters: ", getAvailableLetters(lettersGuessed))
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase in lettersGuessed:
                print("The letter has already been guessed: ", getGuessedWord (secretWord, lettersGuessed))
                
            elif guessInLowerCase not in secretWord:
                print("The letter is not found in the word: ", getGuessedWord (secretWord, lettersGuessed))
                chances-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Great Job!:",getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            print ("Congratulations, you guessed the word!")
            break
        
    else:
        print("------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord)