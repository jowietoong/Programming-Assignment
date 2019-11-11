def getAvailableLetters(lettersGuessed):
    word = ""
    count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter in lettersGuessed:
            count+=1
        else:
            word+=letter
    return word