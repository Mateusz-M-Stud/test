# Function to convert Celsius to Kelvin
def cel_to_kel(celsius):
    return celsius + 273.15

# Function to convert Celsius to Fahrenheit
def cel_to_fahr(celsius):
    return (celsius * 9/5) + 32

def main():
    # Temp in celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Converting to Kelvin and Fahrenheit
    kelvin = cel_to_kel(celsius)
    fahrenheit = cel_to_fahr(celsius)
    
    # Print the results
    print(f"The temperature in Kelvin is: {kelvin:.2f} K")
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f} °F")

# Run the program
if __name__ == "__main__":
    main()