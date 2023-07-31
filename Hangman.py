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
print(random_word) #delete/comment this line

def play():

    hidden_words = [char for char in random_word]
    shown_words = list()
    wrong = 0

    while True:
        hidden_words.sort, shown_words.sort()
        if hidden_words == shown_words:
            print("You Won!")
            break
                
        add = input("\nEnter a guess: ")

        if add in shown_words:
            print(f"{add} already guessed!")
            hidden_words.sort, shown_words.sort()
            if hidden_words == shown_words:
                print("You Won!")
            continue

        elif len(shown_words) == len(hidden_words):
            print("You Won!")
            break
        else:

            if len(add) == 1: #input only one character

                if add in hidden_words:

                    shown_words.append(add)

                    for char in random_word: #print the guessed word and underscores

                        if char in shown_words:
                            print(char, end='')
                        else:
                            print("_", end='')
                else: 
                    wrong +=1
                    print(display(wrong))
                    if wrong == 7:
                        print("Game Over")
                        break
                    continue

            else: #if multiple characters
                print("Please enter only one character!") 

play()