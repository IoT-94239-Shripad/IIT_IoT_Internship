def km_to_m(distance_km):
    
    return distance_km * 1000

def m_to_cm(distance_m):
    
    return distance_m * 100

def cm_to_mm(distance_cm):
    
    return distance_cm * 10

def feet_to_inches(distance_feet):
    
    return distance_feet * 12

def inches_to_cm(distance_inches):
    
    return distance_inches * 2.54

def distance_converter(distance, conversion_type_str, conversion_func):
    
    result = conversion_func(distance)
    print(f"{distance} {conversion_type_str.split(' to ')[0]} is equal to {result:.4f} {conversion_type_str.split(' to ')[1]}")
    return result


if __name__ == "__main__":
    try:
        
        user_input_distance = float(input("Enter a distance value (as a number): "))

        print(f"\n--- Performing all conversions for initial value of {user_input_distance} ---")

        distance_converter(user_input_distance, "km to m", km_to_m)

        distance_converter(user_input_distance, "m to cm", m_to_cm)
        
        distance_converter(user_input_distance, "cm to mm", cm_to_mm)

        distance_converter(user_input_distance, "feet to inches", feet_to_inches)
        
        distance_converter(user_input_distance, "inches to cm", inches_to_cm)

    except ValueError:
        print("Invalid input. Please enter a numerical value for distance.")

