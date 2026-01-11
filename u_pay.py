import random
print ("Let's roll the wheel and select our winner")
names = input("enter name of the participants separated by commas: ")
players = names.split(",")
# print (players[1].strip())
winner = (random.choice(players)).strip()
print (f"The winner is {winner.upper()}")