#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")

# วิธีรันบน Linux:
#   chmod +x downcase_it.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./downcase_it.py | cat -e
#   ./downcase_it.py "LUCIOLE" | cat -e
#   ./downcase_it.py 'This exercise is quite easy!' | cat -e
