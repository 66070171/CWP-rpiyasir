#!/usr/bin/env python3

password = "Python is awesome"

if input() == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

# วิธีรันบน Linux:
#   chmod +x password.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./password.py    (พิมพ์ 1234)
#   ./password.py    (พิมพ์ Python is awesome)
