print ("Welcome to Jurassic Park's Roller Coster Ride")
print ("Input your details to get your ticket")
print ("Price details are as below")
print ("Age 13 & up to 20: 50₹")
print ("Age 21 & up to 30: 100₹")
print ("Age 31 & above: 150₹")
print ("Charger for photo: 50₹")
Name = (input("What is your Name\n"))
Age = int(input("What is your age\n"))
Height = int(input("What is your height\n"))
Weight = int(input("What is your weight\n"))
Ticket = str(input(f"Lastly!! Do you need photo Mr.{Name}\n (press y for Yes & n for No): "))
bmi = Weight / ((Height/100) ** 2)

#Below are the eligibility & final price for the ride
if bmi > 18.5 and Age > 12 and bmi < 50:
  if Age <= 20:
    a=50
  elif Age <= 30:
    a=100
  elif Age > 30:
    a=150
  if Ticket== "n":
    print(f"\nYour ticket price '{a}', Enjoy your ride & BMI is {bmi}\n")
  if Ticket== "y":
    print(f"\nYour ticket price '{int(a)+50}', Enjoy your ride & BMI is {bmi}\n")
else:
  print(f"\nYou have to grow up to ride the ride & BMI is {bmi}\n")
