
converters = [
    lambda t: t * 1000,            
    lambda kg: kg * 1000,           
    lambda g: g * 1000,             
    lambda mg: mg * 0.00000220462   
]

tonnes = float(input("Enter weight in tonnes: "))

kg = converters[0](tonnes)
g = converters[1](kg)
mg = converters[2](g)
lbs = converters[3](mg)

print("Kilograms:", kg, "kg")
print("Grams:", g, "gm")
print("Milligrams:", mg, "mg")
print("Pounds:", lbs, "lbs")
