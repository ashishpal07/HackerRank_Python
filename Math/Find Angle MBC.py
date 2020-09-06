#Find Angle MBC

import math

AB = int(input("Enter AB = "))
BC = int(input("Enter Bc = "))

#Calculating Hypotaneous
H = math.hypot(AB,BC)

#Calculating Angle
A = round(math.degrees(math.acos(BC/H)))

#To get degree symbol
D = chr(176)
print(A,D, sep="")
