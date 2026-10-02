try:
    age = int(input('Enter yore age: '))
except ValueError:
    print('Age must be a interger number!')
except:
    print('Programm error!')
else:
    if age > 150 or age <0:
        print('Incorrect age!')
    elif age >= 18:
        print('Welcome!')
    else:
        print('You need to grow up a little!')
finally:    
    print('Good bye!')
