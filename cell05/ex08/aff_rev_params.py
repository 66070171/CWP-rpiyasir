#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for param in reversed(params):
        print(param)

# วิธีรันบน Linux:
#   chmod +x aff_rev_params.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./aff_rev_params.py | cat -e
#   ./aff_rev_params.py "coucou" | cat -e
#   ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
