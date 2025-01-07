# Finger exercise: Write code that asks the user to enter their
# birthday in the form mm/dd/yyyy, and then prints a string of the
# form ‘You were born in the year yyyy.’

birthday = input('Enter your birthday in the form mm/dd/yyyy: ')
year = birthday[-4:]
print(f'You were born in the year {year}.')