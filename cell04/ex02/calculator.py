#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))

print("Thank you!")

print(first, "+", second, "=", first + second)
print(first, "-", second, "=", first - second)
print(first, "/", second, "=", first / second)
print(first, "*", second, "=", first * second)

# วิธีรันบน Linux:
#   chmod +x calculator.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./calculator.py  (พิมพ์ 10 แล้ว 2)
