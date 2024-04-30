myBill = float(input("How Much is on the bill in dollars?: "))
numberOfPeople = int(input("How many people are there total?: "))
answer = myBill / numberOfPeople
answer = round(answer,2)
print("You all owe", answer)
tip = int(input("How Much Percent would you like to tip:"))
tip = tip / 100
tip = tip * answer
tip = round(tip,2)
print(tip + answer)