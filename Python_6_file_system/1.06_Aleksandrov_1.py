import os

if not os.path.exists(
    "new file.txt"
):  # Провека наличия файла, создание его если он отсутствует
    file = open("new file.txt", "w")
    file.close()

file = open("new file.txt", "r", encoding="utf-8")  # Чтение файла
text = file.read()
file.close()

print("Текущее содержимое файла:")  # Вывод содержимого файла
print(text if text else "(файл пуст)")

new_text = input("Введите текст для добавления в начало файла: ")  # Ввод нового текста

text = new_text + "\n" + text  # Добавляем новый текст в файл в начало файла

file = open("new file.txt", "w", encoding="utf-8")  # Запись в файл
file.write(text)
file.close()

print("Новое содержимое файла:")
print(text)
