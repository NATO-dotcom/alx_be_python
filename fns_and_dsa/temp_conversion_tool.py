FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        temp_input = input("Enter the temperature to convert: ").strip()
        try:
            temp = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")

if __name__ == "__main__":
    main()
