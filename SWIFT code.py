###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
# SWIFT code from the user
swift = input('Enter SWIFT code: ')

# Bank Code (first 4 characters)
bank_code = swift[:4]

# Country Code (next 2 characters)
country_code = swift[4:6]

# Print the results
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')