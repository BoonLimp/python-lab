import math

speed = float(input("Enter the ball speed (km/h): "))
length = float(input("Enter the court length (m): "))
weight = float(input("ENter the ball weight (g): "))
time = 23.8/(speed*10/36)*2
acceleration = ((speed*10/36)/time)
force = acceleration*weight 
displacement = 0.5*acceleration*time**2
energy = force * displacement/1000
calorie = energy/4.184

print("Time = ", time, "Energy = ", energy, "J = ", calorie, "cal")
