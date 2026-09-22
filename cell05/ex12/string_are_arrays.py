#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    found = ""
    for letter in sys.argv[1]:
        if letter == "z":
            found = found + "z"
    if found == "":
        print("none")
    else:
        print(found)

# วิธีรันบน Linux:
#   chmod +x string_are_arrays.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./string_are_arrays.py | cat -e
#   ./string_are_arrays.py "The character Z is not found in this string" | cat -e
#   ./string_are_arrays.py "The character z is found in this string" | cat -e
#   ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
