#!/usr/bin/env python3

num = float(input("Give me a number: "))

if num == int(num):
    print("This number is an integer.")
else:
    print("This number is a decimal.")

# วิธีรันบน Linux:
#   chmod +x float.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./float.py       (พิมพ์ 42)
#   ./float.py       (พิมพ์ 42.00)
#   ./float.py       (พิมพ์ 42.42)
