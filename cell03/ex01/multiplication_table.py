#!/usr/bin/env python3

print("Enter a number")
num = int(input())

for i in range(10):
    print(i, "x", num, "=", i * num)

# วิธีรันบน Linux:
#   chmod +x multiplication_table.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./multiplication_table.py   (พิมพ์ 8)
