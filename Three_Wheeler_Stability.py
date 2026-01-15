# import time
# import random

# input requirements to calculate stability
try:
    print ("Provide below values to calculate stability of given 3 wheeled vehicle")
    wheel_track = int(input("Wheel Track in mm: ")) / 1000 #Value converted to meters
    wheel_base = int(input("Wheel Base in mm: ")) / 1000 #Value converted to meters
    cg_height = int(input("CoG from Ground (Z Dir) in mm: ")) / 1000 #Value converted to meters
    TCD = int(input("TCD in m: "))
    gravity = 9.81 #m/sec2
    print (wheel_base, wheel_track, cg_height)
except ValueError as e:
    print("Enter a numeric value :(")
except ZeroDivisionError as k:
    print("Zero cannot be taken into account :(")

# Calculating Static Roll Over Stability
def static_rollover_stability(wheel_track,cg_height):
    ssf = wheel_track / (2*cg_height)
    return print (f"Your Static Rollover Stability At Standstill / Low Speed is {ssf} ")