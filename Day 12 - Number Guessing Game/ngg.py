import random
import os
logo = '''
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ '''

#Main Function

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")

    print("I Am Thinking Of A Number...(1-100)")
    num = random.randint(1 , 101)
    #print(num) #Testing Only
    count = 10 #Easy by default

    level = input("What Level Would You Like To Play - \"Easy\" or \"Medium\" or \"Hard\"? : ").lower()
    if level == "medium":
        count = 7
    elif level == "hard":
        count = 5
            

    for i in range(0 , count):
        print(f"You Have {count - i} Chances Left.")
        guess = int(input("Guess The Number : "))
        if guess == num:
            print("You Won!")
            print(f"The Number Was {num}")
            return


    print("Oh no! All Your Chances Are Over...You Loose")
    print(f"The Number Was {num}")
    return

visit = True

while visit:
    res = input("Do You Want To Play A Game Of Number Guessing \"Y\" or \"N\": ").lower()
    if res == "y":
        os.system('cls')
        game()
    else:
        print("Good Bye")   
        visit = False 
