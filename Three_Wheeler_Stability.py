# import time
# import random
import math

# input requirements to calculate stability
try:
    print ("Provide below values to calculate stability of given 3 wheeled vehicle")
    wheel_track = int(input("Wheel Track in mm: ")) / 1000 #Value in mm > converted to meters
    wheel_base = int(input("Wheel Base in mm: ")) / 1000 #Value in mm > converted to meters
    cg_height = int(input("CoG from Ground (Z Dir) in mm: ")) / 1000 #Value in mm > converted to meters
    tcd = int(input("TCD in m: "))
    gravity = 9.81 #m/sec2
    # print (wheel_base, wheel_track, cg_height)
except ValueError as e:
    print("Enter a numeric value :(")
except ZeroDivisionError as k:
    print("Zero cannot be taken into account :(")

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
print (round(safe_turning_speed,1),"km/h")