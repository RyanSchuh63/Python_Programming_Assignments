change = int(input('Enter how much change you have in cents. '))
HD = 0
QD = 0
DM = 0
NK = 0
PN = 0 #Input for change and variables for all coins
while change >= 50:
    change = change - 50
    HD =+ 1
while change >= 25:
    change = change - 25
    QD = QD + 1
while change >= 10:
    change = change - 10
    DM = DM + 1
while change >= 5:
    change = change - 5
    NK = NK + 1
while change >= 1:
    change = change - 1
    PN = PN + 1
    #looping statement that increases coin variables runs until change = 0
print("You have", HD, "Half-Dollars,", QD, "Quarters,", DM, "Dimes,", NK,
      "Nickles, and", PN, "Pennies.")#Prints new variable values
