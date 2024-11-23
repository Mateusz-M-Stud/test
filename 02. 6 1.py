###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = input("Enter name: ")   # replace Anna with your name
surname = input("Enter surname: ") # replace May with your surname
characters_in_name = len(name)
x = len(surname)
all = name+surname
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} ')
print(f"Your full name has {len(all)}") # with a space between name and surname