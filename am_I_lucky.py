print (r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
       ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
location = input ("Which would you like to go forest or city? \n").upper()
if (location == "FOREST"):
  crossing=(input("You arrived near a river!!\nYou wish to swim or walk accross\n").upper())
  if crossing == "WALK":
      door = input("Woff!! got away from corcodile and arrived at treasure door\n"
      "Choose any one door RED/BLUE/GREEN\n").upper()
      if door == "RED":
          print ("Congradulation!!!! you won the treasure")
      elif door == "GREEN":
          print ("You Fell in to a fire pit, GameOver")
      elif door == "BLUE":
          print ("You were ate by lion, GameOver")
      else:
          print ("Select correct door!!, Start again")
else:
    if location == "CITY":
        print ("You ran over by truck, GameOver")
    elif location != "CITY" or location != "FOREST":
        print ("You got lost either goto forest or city")
        