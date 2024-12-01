
import math

def main():
    print("Welcome to QuickCalc!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("Enter calculation or command: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            # Check for unit conversions
            if "to" in user_input:
                convert_units(user_input)
            else:
                # Evaluate mathematical expression
                result = eval(user_input, {"__builtins__": None}, math.__dict__)
                print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def convert_units(input_string):
    try:
        # A basic unit conversion (extend as needed)
        parts = input_string.split("to")
        value_with_unit = parts[0].strip()
        target_unit = parts[1].strip()

        value, current_unit = value_with_unit.split()
        value = float(value)

        if current_unit == "cm" and target_unit == "m":
            print(f"{value} cm = {value / 100} m")
        elif current_unit == "m" and target_unit == "cm":
            print(f"{value} m = {value * 100} cm")
        elif current_unit == "kg" and target_unit == "g":
            print(f"{value} kg = {value * 1000} g")
        elif current_unit == "g" and target_unit == "kg":
            print(f"{value} g = {value / 1000} kg")
        else:
            print("Unsupported conversion.")
    except Exception as e:
        print(f"Invalid conversion format. Example: '100 cm to m'. Error: {e}")

if __name__ == "__main__":
    main()
