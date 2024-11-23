###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
# Get the age from the user
age = int(input('Enter age: '))

# Check if the person is exempt
no_tax = age <= 26  # People up to and including 26 are exempt
print(f'Exemption from paying taxes: {no_tax}')

# Test the program with the provided data
test_ages = [38, 27, 26, 22, 18]
print("\nTesting the program with sample ages:") # \n break
for test_age in test_ages:
    print(f"Age: {test_age}, Exempt: {test_age <= 26}")