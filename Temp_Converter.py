
#Formula for celsius to F: (32°F − C) × 5/9 = 0°C
#Formula for Fahrenheit to Celsius: °C = (°F - 32) × 5/9

conversion = str(input("Enter the type of temperature your want to convert: (for eg: C to F or F to C): "))
if(conversion == "C to F"):
    temp1 = float(input("Enter the Temperature in Celsius: "))
    sol1 = (temp1 * 9/5) + 32
    print(f"{temp1}°C in fahrenheit is: {sol1}°F")

else:
    temp2 = float(input("Enter the Temperature in Fahrenheit: "))
    sol2 = (temp2 - 32) * 5/9
    print(f"{temp2}°F in Celsius is: {sol2}°C")





 
