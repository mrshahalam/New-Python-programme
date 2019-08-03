"""
Convert Temperature
1. Celsius to Farenheit
2. Farenheit to Celsius
"""
print("\tTEMPERATURE CONVERTER CONSOLE APP")
print("------------------------------------------------")
print("TEMPERATURE CONVERSION FROM CELSIUS TO FARENHEIT")

celsius1 = float(input("Enter the temperature in Celsius: "))

farenheit1 = (celsius1 * 9/5) + 32

print("The temperature in Farenheit is: ", farenheit1)

print("TEMPERATURE CONVERSION FROM FARENHEIT TO CELSIUS")

farenheit2 = float(input("Enter the temperature in Farenheit: "))

celsius2 = (farenheit2 - 32) * 5/9

print("The temperature in Celsius is: ", celsius2)
