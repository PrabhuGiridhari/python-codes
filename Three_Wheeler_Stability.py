# import time
# import random
import math
from math import radians

# Function to force user to provide valid inputs
def valid_number(prompt,min_val,max_val):
    while True:
        user_input = input(prompt)
        try:
            user_val = int(user_input)
            if min_val <= user_val <= max_val:
                return user_val
            else:
                print ("Please enter a number between " + str(min_val) + " and " + str(max_val))
        except ValueError:
            print ("Please enter a number between " + str(min_val) + " and " + str(max_val))

# input requirements to calculate stability
print ("Provide below values to calculate stability of given 3 wheeled vehicle")
wheel_track = valid_number("Wheel Track in mm: ",1,2600) /1000 #Value in mm > converted to meters
wheel_base = valid_number("Wheel Base in mm: ",1,18000) /1000 #Value in mm > converted to meters
cg_height = valid_number("CoG from Ground (Z Dir) in mm: ",1,18000) /1000 #Value in mm > converted to meters
handlebar_angle = valid_number("Handlebar input angle (values with in range 1~52\N{DEGREE SIGN}): ",1,52)
proposed_speed = valid_number("Proposed vehicle speed during turing:",1,60)
gravity = 9.81 #m/sec2

# Arriving TCD to Steering angle
tcd = wheel_base / math.sin(radians(handlebar_angle))

# Calculating Static Roll Over Stability
def static_rollover_stability(a,b):
    value = a / (2 * b)
    return round(value,3)
ssf = static_rollover_stability(wheel_track, cg_height)
if ssf >= 1:
    print(f"Your Static Rollover Stability value is {ssf}g, Excellent. \nNote: Any value greater or equal to 1 is excellent")
elif 0.8 <=ssf <= 1:
    print(f"Your Static Rollover Stability value is {ssf}g, Good. \nNote: Any value in between 0.8 ~ 0.99 is acceptable")
else:
    print(f"Your Static Rollover Stability value is {ssf}g, Not Good. \nNote: Any value below 0.8 is at risk of rolling")

# Calculating Critical Lateral Acceleration & it is also known as Static Roll Over Stability
critical_lateral_acceleration = ssf * gravity #output value in m/sec2

# Calculating Safe turning speed for your vehicle geometry
safe_turning_speed = math.sqrt(critical_lateral_acceleration * tcd) * 3.6 # Multiply by 3.6 to convert m/sec2 to Km/h
if proposed_speed <= safe_turning_speed:
    print(f"Your vehicle speed is {proposed_speed}, if u turn vehicle handle bar to {handlebar_angle}\N{DEGREE SIGN} angle")
    print(f"you will experience {ssf}g & your vehicle is in safe stability")
else:
    print(f"Your vehicle speed is {proposed_speed}, if u turn handle bar to {handlebar_angle}\N{DEGREE SIGN} angle")
    print(f"you will experience {ssf}g & Caution!!!! Vehicle will topple")

input("Press ENTER to continue")# To pause and show the result
