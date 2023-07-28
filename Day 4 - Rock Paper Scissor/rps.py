import random
print("Welcome To The Rock Paper Scissor Game")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


resp = int(input("What is Your Response (1=Rock 2=Paper 3=Scissor) : "))

print("Your Response is :")
if resp == 1:
    print(rock)
elif resp == 2 :
    print(paper)
else :
    print(scissors) 


pc_resp = random.randint(1,3)
print("Computer's Response is :")
if pc_resp == 1:
    print(rock)
elif pc_resp == 2 :
    print(paper)
else :
    print(scissors)


#Winning or loosing
if pc_resp==1 and resp==3:
    print("You Loose PC wins")
elif pc_resp > resp:
    print("You Loose PC Wins")
elif pc_resp == resp:
    print("Draw Match")
elif pc_resp < resp:
     print("You Win PC loose")        

    