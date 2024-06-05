import math

num = float(input("Enter #possible states: "))
result = math.log(num, 2)
result = math.ceil(result)
print(result)