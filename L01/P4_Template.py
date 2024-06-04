initial = float(input("Starting balance: "))
time = float(input("years: "))
rate = float(input("average interest rate: "))
money = initial* (1+ rate/100)**time
print(money)