km_to_m =  lambda dist: dist * 1000
m_to_cm =  lambda dist: dist * 100
cm_to_mm = lambda dist: dist * 10
feet_to_inches = lambda dist: dist * 12
inches_to_cm = lambda dist: dist * 2.54

def distance_converter(distance, conversion_type, conversion_func):
    
    result = conversion_func(distance)
    print(f"{distance} {conversion_type.split(' to ')[0]} is equal to {result:.2f} {conversion_type.split(' to ')[1]}.")

while True:
    try:
        user_distance_input = float(input("Enter a distance : "))
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

print("\n--- All Conversions for the Input Distance ---")
distance_converter(user_distance_input, "km to m", km_to_m)
distance_converter(user_distance_input, "m to cm", m_to_cm)
distance_converter(user_distance_input, "cm to mm", cm_to_mm)
distance_converter(user_distance_input, "feet to inches", feet_to_inches)
distance_converter(user_distance_input, "inches to cm", inches_to_cm)


