#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

# วิธีรันบน Linux:
#   chmod +x greetings_for_all.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./greetings_for_all.py | cat -e
