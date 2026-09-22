#!/usr/bin/env python3

print("Enter a number less than 25")
num = int(input())

if num > 25:
    print("Error")
else:
    for i in range(num, 26):
        print("Inside the loop, my variable is", i)

# วิธีรันบน Linux:
#   chmod +x to25.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./to25.py        (พิมพ์ 45)
#   ./to25.py        (พิมพ์ 20)
