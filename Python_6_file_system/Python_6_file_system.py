import os

if not os.path.exists("new file.txt"):
    file = open("new file.txt", "w")
    file.close()
file = open("new file.txt", "r")
text = file.read()
text = "new text\n" + text
file.close()
file = open("new file.txt", "w")
file.write(text)
file.close()
