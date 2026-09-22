#!/usr/bin/env python3

num = int(input())

if num < 0:
    print("This number is negative.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")

# วิธีรันบน Linux:
#   chmod +x isneg.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./isneg.py       (พิมพ์ 42)
#   ./isneg.py       (พิมพ์ -42)
#   ./isneg.py       (พิมพ์ 0)
