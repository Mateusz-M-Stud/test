def cm_to_feet_and_inches(cm):
    # 1 foot = 30.48 cm, 1 inch = 2.54 cm
    feet = cm // 30.48
    remaining_cm = cm % 30.48
    inches = remaining_cm // 2.54
    return feet, inches

def main():
    cm = float(input("Enter your height in centimeters: "))
    # Convert to feet and inches
    feet, inches = cm_to_feet_and_inches(cm)
    
    print(f"Your height in centimeters: {cm:.2f} cm")
    print(f"Your height in feet and inches: {feet} feet {inches} inches")

if __name__ == "__main__":
    main()