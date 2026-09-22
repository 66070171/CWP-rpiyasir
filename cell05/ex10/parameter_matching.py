#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    word = input("What was the parameter? ")
    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

# วิธีรันบน Linux:
#   chmod +x parameter_matching.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./parameter_matching.py
#   ./parameter_matching.py "Hello"   (พิมพ์ Bonjour)
#   ./parameter_matching.py "Hello"   (พิมพ์ Hello)
