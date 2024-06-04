note = int(input("The first note: "))
num = [0, 0, 0]
i = 0
num1 = 0
while i < 3:
    if note + num1 > 7:
        note = 0
        num1 = 2
    num[i] = note + num1
    num1 = num1 + 2
    i = i+1
print("Trial: ", num)    

