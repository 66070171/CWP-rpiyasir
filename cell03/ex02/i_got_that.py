#!/usr/bin/env python3

answer = input("What you gotta say? : ")

while answer != "STOP":
    answer = input("I got that! Anything else? : ")

# วิธีรันบน Linux:
#   chmod +x i_got_that.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./i_got_that.py  (พิมพ์ Hello / I like ponies / stop... / STOP)
