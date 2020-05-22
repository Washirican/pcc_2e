# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-21
# --------------------------------------------------------------------------- #

print('Enter two numbers and I\'ll add them.')
print('Enter \'q\' to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break

    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Please, enter a number!')
    else:
        print(f'The sum of {first_number} and {second_number} is {result}.')

