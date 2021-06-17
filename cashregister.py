item1 = float(input("Enter price of the first item: "))
item2 = float(input("Enter price of the second item: "))

print("Does customer have a club card? (Y/N)")
club_card_member = input()

def check_club_membership(club_card_member):
    if(club_card_member == "y" or club_card_member == "Y"):
         return("yes")
    elif(club_card_member == "n" or club_card_member == "N"):
        return("no")
    elif club_card_member != "n" or club_card_member != "y":
        print(club_card_member, "is an invalid input.")
        return("club card registration went wrong!")   

club_card_member = check_club_membership(club_card_member)

tax_rate = float(input("Enter tax rate: "))
tax_rate = round(tax_rate,2)

base_price = item1 + item2
price_no_member = 0.0

if(item1 < item2):
    tmp_item1 = item1 / 2
    price_no_member = tmp_item1 + item2
else:
    tmp_item2 = item2 / 2
    price_no_member = tmp_item2 + item1

price_no_member = round(price_no_member)

price_after_discounts = 0.0
price_with_tax = 0.0

if club_card_member == "no":
    price_after_discounts = price_no_member
    price_with_tax = price_after_discounts + ((price_after_discounts / 100) * tax_rate)    
else:    
    price_after_discounts = ((price_no_member - (price_no_member /100) * 10))
    price_with_tax = (price_after_discounts + ((price_after_discounts / 100) * tax_rate))
    
price_with_tax = round(price_with_tax,2)

print("Base price =", base_price)
print("Price after discounts =",price_after_discounts)
print("Total price =", price_with_tax)
