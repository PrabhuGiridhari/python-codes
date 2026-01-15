import time
import random

# input requirements to calculate stability
try:
    print ("Provide below values to calculate stability of given 3 wheeled vehicle")
    wheel_track = int(input("Wheel Track in mm: ")) / 1000 #Value converted to meters
    wheel_base = int(input("Wheel Base in mm: ")) / 1000 #Value converted to meters
    CG_Height = int(input("CoG from Ground (Z Dir) in mm: ")) / 1000 #Value converted to meters
    TCD = int(input("TCD in m: "))
    gravity = 9.81 #m/sec2
    print (wheel_base, wheel_track, CG_Height)
except ValueError as e:
    print("Enter a numeric value :(")
except ZeroDivisionError as e:
    print("Zero cannot be taken into account :(")

# Calculating Static Roll Over Stability
def Static_Rollover_Stability(a,b):
    SSF = a / 2b
    return print (f"Your Static Rollover Stability At Standstill / Low Speed is {SSF} ")