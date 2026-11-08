temperature = float(input("Enter temperature (F): "))
temperatureC = (temperature-32) * 5/9
speed = (331 + 0.6 * temperatureC)
print("Sound travels at: " + str(speed) + (" ms"))