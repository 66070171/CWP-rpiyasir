#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        line = "Table de " + str(i) + ":"
        j = 0
        while j <= 10:
            line = line + " " + str(i * j)
            j = j + 1
        print(line)
        i = i + 1

# วิธีรันบน Linux:
#   chmod +x advanced_mult.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./advanced_mult.py "yolo" | cat -e
#   ./advanced_mult.py
