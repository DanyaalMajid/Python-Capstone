from forex_python.converter import CurrencyRates

def convert_temp(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        converted_value = (value * 9/5) + 32
        return converted_value
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        converted_value = (value - 32) * 5/9
        return converted_value
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        converted_value = value + 273.15
        return converted_value
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        converted_value = value - 273.15
        return converted_value
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        converted_value = (value - 32) * 5/9 + 273.15
        return converted_value
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        converted_value = (value - 273.15) * 9/5 + 32
        return converted_value
    
    else:
        print("Invalid temperature conversion")
        return None

def convert_currency(from_unit, to_unit, value):
    c = CurrencyRates()
    converted_value = c.convert(from_unit, to_unit, value)
    if converted_value is not None:
        return converted_value
    else:
        print("Invalid currency conversion")
        return None
    
def convert_volume(from_unit, to_unit, value):
    if from_unit == "Gallons" and to_unit == "Liters":
        converted_value = value * 3.78541
        return converted_value
    elif from_unit == "Liters" and to_unit == "Gallons":
        converted_value = value / 3.78541
        return converted_value
    elif from_unit == "Gallons" and to_unit == "Cubic Meters":
        converted_value = value / 264.172
        return converted_value
    elif from_unit == "Cubic Meters" and to_unit == "Gallons":
        converted_value = value * 264.172
        return converted_value
    elif from_unit == "Liters" and to_unit == "Cubic Meters":
        converted_value = value / 1000
        return converted_value
    elif from_unit == "Cubic Meters" and to_unit == "Liters":
        converted_value = value * 1000
        return converted_value
    
    else:
        print("Invalid volume conversion")
        return None

def convert_mass(from_unit, to_unit, value):
    if from_unit == "Pounds" and to_unit == "Kilograms":
        converted_value = value * 0.453592
        return converted_value
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        converted_value = value / 0.453592
        return converted_value
    elif from_unit == "Pounds" and to_unit == "Grams":
        converted_value = value * 453.592
        return converted_value
    elif from_unit == "Grams" and to_unit == "Pounds":
        converted_value = value / 453.592
        return converted_value
    elif from_unit == "Kilograms" and to_unit == "Grams":
        converted_value = value * 1000
        return converted_value
    elif from_unit == "Grams" and to_unit == "Kilograms":
        converted_value = value / 1000
        return converted_value
    
    else:
        print("Invalid mass conversion")
        return None

def main():
    while True:
        print("1. Temperature Conversion")
        print("2. Currency Conversion")
        print("3. Volume Conversion")
        print("4. Mass Conversion")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            from_unit = input("Enter the from unit: ")
            to_unit = input("Enter the to unit: ")
            value = float(input("Enter the value: "))
            converted_value = convert_temp(from_unit, to_unit, value)
            if converted_value is not None:
                print(f"Converted value: {converted_value}")
        
        elif choice == "2":
            from_unit = input("Enter the from unit: ")
            to_unit = input("Enter the to unit: ")
            value = float(input("Enter the value: "))
            converted_value = convert_currency(from_unit, to_unit, value)
            if converted_value is not None:
                print(f"Converted value: {converted_value}")
        
        elif choice == "3":
            from_unit = input("Enter the from unit: ")
            to_unit = input("Enter the to unit: ")
            value = float(input("Enter the value: "))
            converted_value = convert_volume(from_unit, to_unit, value)
            if converted_value is not None:
                print(f"Converted value: {converted_value}")
        
        elif choice == "4":
            from_unit = input("Enter the from unit: ")
            to_unit = input("Enter the to unit: ")
            value = float(input("Enter the value: "))
            converted_value = convert_mass(from_unit, to_unit, value)
            if converted_value is not None:
                print(f"Converted value: {converted_value}")
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()