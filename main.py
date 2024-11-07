myBill = float(input("What was the bill?: "))
tip = int(input("What percentage do you want to tip?: "))
numberOfPeople = int(input("How many people?: "))
percent = tip / 100
bill = myBill * percent
total = bill + myBill
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
