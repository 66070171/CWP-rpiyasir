#!/usr/bin/env python3

import sys

def downcase_it(text):
    return text.lower()

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for param in params:
        print(downcase_it(param))

# วิธีรันบน Linux:
#   chmod +x downcase_all.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./downcase_all.py
#   ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
