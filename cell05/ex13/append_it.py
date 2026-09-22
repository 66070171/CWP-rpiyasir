#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")

# วิธีรันบน Linux:
#   chmod +x append_it.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./append_it.py | cat -e
#   ./append_it.py "parallel" "egoism" "human" | cat -e
