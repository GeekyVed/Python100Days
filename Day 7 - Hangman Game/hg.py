import random
hmantitle = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      '''

h_s0 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

word_list = [
    "python",
    "hangman",
    "programming",
    "computer",
    "algorithm",
    "variable",
    "function",
    "loop",
    "conditional",
    "dictionary",
    "list",
    "string",
    "integer",
    "float",
    "boolean",
    "class",
    "object",
    "module",
    "package",
    "import",
    "inheritance",
    "polymorphism",
    "encapsulation",
    "abstraction",
    "exception",
    "debugging",
    "iteration",
    "recursion",
    "database",
    "web",
    "server",
    "client",
    "interface",
    "framework",
    "library",
    "data",
    "analysis",
    "visualization",
    "machine",
    "learning",
    "artificial",
    "intelligence",
    "neural",
    "network",
    "deep",
    "learning",
    "cloud",
    "security",
    "encryption",
    "authentication",
    "authorization",
]

h_s1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

h_s2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''

h_s3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''

h_s4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''

h_s5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

h_s6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

h_s7 = '''
  +---+
  |   |
  O   |
 /|\  |
_/ \  |
      |
=========
'''

h_s8 = '''
  +---+
  |   |
  O   |
 /|\  |
_/ \_ |
      |
=========
'''
h_s = [h_s0 , h_s1 , h_s2 , h_s3 , h_s4 , h_s5 , h_s6 , h_s7 , h_s8]

print(hmantitle)
#Keeping Track of LIVES
lives = 8
eog = False

#Choosing Word
chosen_word = random.choice(word_list)

#Testing Code
#print(f"PSSST...THE CHOSEN WORD IS {chosen_word}")

#Making an Empty list
chosen_word_l = len(chosen_word)
display = []
for i in range(0 , chosen_word_l):
    display.append("_")
print(display)



while not eog :
    #Guess the letter
    guess = input("Enter your guess letter : ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}\n")

    #Check Matching
    for i in range(chosen_word_l ):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives-=1
        if lives == 0:
            eog = True
            print("YOU LOOSE!!!\n")

    print(f"{' '.join(display)}")    

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!! \n")


    print(h_s[8-lives])


