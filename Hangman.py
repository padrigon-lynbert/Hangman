import random
import os

words = story = """ 
In a hidden forest, a courageous young sorceress stumbled upon a mystical amulet.
As she wore it, whispers of ancient magic consumed her, granting incredible powers. 
But with great power came a daunting choice: use it for good or succumb to darkness.
Her destiny began, teetering on a delicate thread.
""".lower().split() #lowercase story is now inside words=[] put as word 

words = [word.strip('.,:') for word in words] #remove special chars
exclude_words = ["do", "a", "in", "as", "on", "it", "or", "to", "of", "for", "with", "she", "her", "but"] #specify what to exclude
words = [word for word in words if word not in exclude_words] #remove excluded

def display(wrong):
    
    result = {
    1:str("\t+---+\n\
        |\n\
        |\n\
        |\n\
        |\n\
       ==="),
            
    2:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |\n\
        |\n\
       ==="),

    3:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |   |\n\
        |\n\
       ==="),
    4:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |  /|\n\
        |\n\
       ==="), 
    5:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |  /|\\\n\
        |\n\
       ==="),
    6:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |  /|\\\n\
        |  / \n\
       ==="),
    7:str("\t+---+\n\
        |   |\n\
        |   O\n\
        |  /|\\\n\
        |  / \\\n\
       ===")}
    
    return result[wrong]

random_word = random.choice(words)

def play():
    hidden_words = [char for char in random_word]
    shown_words = ["_" for _ in hidden_words]  # Initialize shown_words with underscores
    wrong_guesses = list()
    wrong = 0

    while True:
        print(f"\nAlready guessed: {wrong_guesses}{shown_words}")

        if "".join(hidden_words) == "".join(shown_words):
            print("\n\nYou Won!")
            break

        add = input("\nEnter a guess: ")

        if len(add) != 1:  # Check for single character input
            print("\nPlease enter only one character!")
            continue

        if add in shown_words:
            print(f"\n{add} already guessed!")
        else:
            if add in hidden_words:
                # Update the shown_words list with the guessed character in the correct positions
                for i, char in enumerate(hidden_words):
                    if char == add:
                        shown_words[i] = add
            else:
                wrong_guesses.append(add)
                wrong += 1
                print(display(wrong))
                if wrong == 7:
                    print("\n\nGame Over")
                    break

        # Display the guessed word and underscores
        for char in shown_words:
            print(char, end='')

play()
