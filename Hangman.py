def Main():
    print("Welcome to Hangman!")
    correct_phrase = Get_Phrase()
    guess_phrase = Setup_Guess_Phrase(correct_phrase)

    #This is to put enough blank print statements to prevent Player 2
    #from automatically seeing the hangman phrase
    for x in range(50):
        print()

    Play_Hangman(correct_phrase, guess_phrase)

def Get_Phrase():
    correct_phrase = ""
    while len(correct_phrase) == 0:
        correct_phrase = input("Player 1, enter a word/phrase for Player 2 to guess: ")
    return correct_phrase.upper()

def Setup_Guess_Phrase(cp):
    guess_phrase = ""
    for x in range(len(cp)):
        if cp[x].isalpha():
            guess_phrase += "_"
        else:
            guess_phrase += cp[x]
    return guess_phrase

def Play_Hangman(cp, gp):
    correct_phrase = cp
    guess_phrase = gp
    num_bad_guesses = 0

    running = True
    while running:
        print("Hangman Phrase: " + guess_phrase)
        Print_Hangman_Body(num_bad_guesses)

        if correct_phrase == guess_phrase:
            print("Congratulations, you guessed the phrase! Player 2 wins!")
            running = False
            continue
        if num_bad_guesses == 6:
            print("Sorry, you lost the game. Player 1 wins!")
            running = False
            continue

        print()
        print("Main Menu:")
        print("0: Guess a Letter.")
        print("1: Guess the hangman phrase.")
        print("2: Quit.")

        user_choice = input()

        if user_choice == "0":
            guess_temp = Guessing_Letter(correct_phrase, guess_phrase)
            if guess_phrase == guess_temp:
                num_bad_guesses += 1
            guess_phrase = guess_temp
        elif user_choice == "1":
            got_it_right = Guessing_Phrase(correct_phrase)
            if got_it_right == True:
                running = False
            else:
                num_bad_guesses += 1            
        elif user_choice == "2":
            running = False
        else:
            print("Input a valid response.")

def Guessing_Letter(cp, gp):
    letter = ""
    while len(letter) != 1:
        letter = input("Type in the letter you want to guess: ")

    guess_phrase_list = list(gp)
    for x in range(len(cp)):
        if cp[x] == letter.upper():
            guess_phrase_list[x] = letter.upper()

    guess_phrase = "".join(guess_phrase_list)

    return guess_phrase

def Guessing_Phrase(cp):
    guess = input("Type in your guess for the hangman phrase: ")
    if guess.upper() == cp:
        print("Congratulations, you guessed the phrase! Player 2 wins!")
        return True
    else:
        print("That's incorrect; try again.")
        return False

def Print_Hangman_Body(nbg):
    print()
    print("          -------")
    print("         |       |")
    print("         |       |")

    if nbg == 0:
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
    elif nbg == 1:
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
        print("                 |")
    elif nbg == 2:
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("         |       |")
        print("                 |")
        print("                 |")
    elif nbg == 3:
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("         |       |")
        print("       \ |       |")
        print("        \|       |")
        print("         |       |")
        print("                 |")
        print("                 |")
    elif nbg == 4:
        print("         |       |")
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("         |       |")
        print("       \ | /     |")
        print("        \|/      |")
        print("         |       |")
        print("                 |")
        print("                 |")
    elif nbg == 5:
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("         |       |")
        print("       \ | /     |")
        print("        \|/      |")
        print("         |       |")
        print("        /        |")
        print("       /         |")
    elif nbg == 6:
        print("        ___      |")
        print("       /   \     |")
        print("       \___/     |")
        print("         |       |")
        print("       \ | /     |")
        print("        \|/      |")
        print("         |       |")
        print("        / \      |")
        print("       /   \     |")

    print("                 |")
    print("                 |")
    print("                 |")
    print("          _______________")

Main()
