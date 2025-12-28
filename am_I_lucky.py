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
  print ("hi")
if location != "CITY" or location != "FOREST":
      print ("You got lost either goto forest or city")
else:
   print("You ran over a truck, you lost")