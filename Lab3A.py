#Class:CSE 1321L
#Section:B10
#Term:Fall 2026
#Instructor:Lan Vu
#Name:Dyllan Brooks
#Lab:1A
currentBalance = float(input("Enter amount owed:"))
apr1 = float(input("Enter Annual Percentage Rate:"))
apr2 = apr1/100
monthlyPercent = apr1/12
minimumPay = currentBalance * apr2 / 12
print("Amount owed: $"+ str(currentBalance))
print("APR: " + str(apr1))
print("Monthly percentage rate: "+str(round(monthlyPercent,3)))
print("Minimum payment: $" + str(round(minimumPay,2)))