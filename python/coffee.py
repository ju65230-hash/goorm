# coffee.py

coffee=10
while True:
    money=int(input("Insert money.: "))
    if money==300:
        print("Dispense coffee.")
        coffee-=1
    elif money>300:
        print("Return %d change, dispense coffee." %(money-300))
        coffee-=1
    else:
        print("Return payment, no coffee dispensed.")
        print("%d coffees left." %coffee)
    if coffee==0:
        print("Out of coffee. Sales stopped.")
        break
    
