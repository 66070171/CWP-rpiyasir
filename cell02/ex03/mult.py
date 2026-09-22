#!/usr/bin/env python3

print("Enter the first number:")
first = int(input())
print("Enter the second number:")
second = int(input())

result = first * second

print(first, "x", second, "=", result)

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

# วิธีรันบน Linux:
#   chmod +x mult.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./mult.py        (พิมพ์ 42 แล้ว 42)
#   ./mult.py        (พิมพ์ 78 แล้ว -1)
#   ./mult.py        (พิมพ์ 72 แล้ว 0)
