price = int(input("price: "))
given = int(input("a customer gives"))
change = given - price 
changeList = [0, 0, 0, 0, 0, 0, 0]
if change < 0:
    print("Please pay more money")
while change >= 500:
    changeList[0] = changeList[0] + 1
    change = change - 500
while change >= 100:
    changeList[1] = changeList[1] + 1
    change = change - 100
while change >= 50:
    changeList[2] = changeList[2] + 1
    change = change - 50    
while change >= 20:
    changeList[3] = changeList[3] + 1
    change = change - 20
while change >= 10:
    changeList[4] = changeList[4] + 1
    change = change - 10
while change >= 5:
    changeList[5] = changeList[5] + 1
    change = change - 5
while change >= 1:
    changeList[6] = changeList[6] + 1
    change = change - 1
print(changeList)