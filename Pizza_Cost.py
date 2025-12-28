# Price details as below
# Small pizza (S): ₹15
# Medium pizza (M): ₹20
# Large pizza (L): ₹25
# Add pepperoni for small pizza (Y or N): +₹2
# Add pepperoni for medium or large pizza (Y or N): +₹3
# Add extra cheese for any size pizza (Y or N): +₹1

print ("Welcome to Prabhu's Pizza Corner")
print ("Tell us how we can make your pizza perfect!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == 'S' or size == 's':
    price += 15
    if pepperoni == "Y" or pepperoni == "y":
        price += 2
    if extra_cheese == "Y" or extra_cheese == "y":
        price += 1
    print (f"Your final bill is: ₹{price}")

else:
    if size == 'M' or size == 'm':
        price += 20
    elif size == 'L' or size == 'l':
        price += 25
    elif size != 'S' and size != 's' and size != 'M' and size != 'm' and size != 'L' and size != 'l':
        print("Invalid size selected.")
    if pepperoni == "Y" or pepperoni == "y":
        price += 3
    if extra_cheese == "Y" or extra_cheese == "y":
        price += 1
    print (f"Your final bill is: ₹{price}")
