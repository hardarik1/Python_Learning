while True:
    try:
        age = int(input('Enter your age: '))
        if not 0 < age < 150:
             print('Incorrect age!')
        elif age >= 18:
             print('Welcome!')
             break 
        else:
             print('Come back later!')
             break
    except TypeError:
        print('Age must be a number!')
    print(f'Next year you\'ll be {age + 1} years old.')