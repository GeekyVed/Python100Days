print("Welcome To The Tip Calculator")
bill = float(input("What is The Bill Amount : $"))
percent_tip = float(input("Enter The Percentage of tip : "))
pepl = int(input("Enter The Number of People : "))
final = bill*(1+(percent_tip/100))/pepl
print(f"The Amount of BiLL is {bill} and the number of people to split is {pepl} with tip percentage of {percent_tip}\nEach Person has to pay ${final}")