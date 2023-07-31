import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def input_data(name , bid , dic):
    dic[name] = bid
    

print(logo)
print("Welcome to The Blind Auction\n")

check = False
while not check :
    dic = {}

    #Taking all bid entries
    should_end = False
    while not should_end:
        name = input("What is your name : ").lower()
        bid = int(input("What is you bid : "))

        input_data(name , bid , dic)

        op = input("Are There Any Other People? \"Yes\" or \"No\" : ").lower()
        if op == "no" or op == "n":
            should_end = True
            print("Bidding Ends...")  
        else :
            # Clearing the Screen
            os.system('cls')

    #Finding Biggest bid
    max = 0
    mk = 0
    for keys in dic:
        if max < dic[keys]:
            max = dic[keys]
            mk = keys

    print(f"The Highest Bid is by {mk} with amount of ${max}")        

    chec = input("Do You want to start another round? \"Yes\" or \"No\" : ").lower()
    if chec == "no" or chec == "n":
            check = True
            