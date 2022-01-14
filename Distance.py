import math

a=input("enter first coordinate : ")

p1 = a.split(",")

b=input("enter second coordinate : ")

p2 = b.split(",")

distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )

print("distance between ", a,"and", b, "is",distance) 
 
