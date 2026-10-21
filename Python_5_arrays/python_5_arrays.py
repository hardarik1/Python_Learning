list = ["2", "!", "w", "W", 1]
list.append(input("Enter new element: "))
list.remove(1)
print(list)
while True:
    indexToDelete = int(input("Which number element you want to remove? "))
    if indexToDelete > len(list):
        print(f"List contain only {len(list)} elements!")
    elif indexToDelete <= 0:
        print("Elemets numbers start with 1! ")
    else:
        list.pop(indexToDelete - 1)
        break
print(list)
print(min(list))
print(max(list))
print(list.pop())

tuple = (2, 1, 3)
print(tuple)
print(min(tuple))
print(max(tuple))
print(sorted(tuple))
print(tuple[0])
print(tuple)

set = {2, 1, 4, 9}
set.add(0)
print(set)
set.pop()
set.remove(4)
set.discard(5)
print(set)

dictionary = {1: 999, 99: 333, 10: 555}
print(dictionary)
print(sorted(dictionary))
print(min(dictionary))
print(max(dictionary))
dictionary[50] = 888
print(dictionary[50])

string = "xwyz"
print(string)
print(string[1])
print(sorted(string))

""" Arrays:
list =  [] - список
tuple = (x, y) - неизменяемый список
set = {x, y} - массив без индекса и индикаторов
dictionary = {1: x, 2: y} - прописывать в ручную индексы
string = 'text' = ()'t', 'e', 'x', 't')
"""
