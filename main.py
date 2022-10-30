import os
user = os.getenv("USERPROFILE")
filename = user + "\\Desktop\\file.txt"
f = open(filename, "w", encoding="utf-8")
f.write("Скоро стану программистом!\n")
f.write("Но это не точно!")
