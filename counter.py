print("Please enter the number of coins: ")
quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))

cents = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies)
dollars = cents // 100
cent = cents % 100

print("The total is", dollars, "dollars and", cent, "cents")