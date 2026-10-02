""" Variable name rules
1) Can contain a-zA-Z0-9_
2) Must begin with a-zA-Z_
3) can't match with reserved names
4) can't contain spaces, use under_score or camelCase instead

"""
age = int(input('Enter your age: '))
if 150 >= age >= 18:
    msg = 'Welcome!'
elif age > 150 or age < 0:
    msg = 'Age is incorrect!'   
else:
    msg = 'You need to grow up a little!'    
print(msg)