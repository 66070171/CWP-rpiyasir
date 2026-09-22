#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print("parameters:", len(params))
    for param in params:
        print(param + ":", len(param))

# วิธีรันบน Linux:
#   chmod +x count_it.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./count_it.py | cat -e
#   ./count_it.py "Game" "of" "Thrones" | cat -e
