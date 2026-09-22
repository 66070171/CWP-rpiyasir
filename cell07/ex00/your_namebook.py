#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    for first_name in persons:
        last_name = persons[first_name]
        full_names.append(first_name.capitalize() + " " + last_name.capitalize())
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

# วิธีรันบน Linux:
#   chmod +x your_namebook.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./your_namebook.py
