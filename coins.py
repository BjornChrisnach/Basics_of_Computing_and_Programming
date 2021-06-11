print("Please enter the amount of money to convert: ")
dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

total_cents = ((dollars * 100) + cents)

quarters = total_cents // 25

mod = total_cents % 25
dimes, nickels, pennies = 0, 0, 0

if mod >= 20:
    dimes = 2
elif mod >= 10:
    dimes = 1
if mod >= 15 and mod <= 19:
    nickels = 1
elif mod >=5 and mod <= 9:
    nickels = 1
if mod >= 1 and mod < 5:
    pennies = mod
elif mod >= 11 and mod <= 14:
    pennies = mod - 10
elif mod >= 16 and mod <= 19:
    pennies = mod - 15
elif mod >= 21 and mod <= 24:
    pennies = mod - 20

print("The coins are", quarters, "quarters,", dimes, "dimes",\
nickels, "nickels and", pennies, "pennies")