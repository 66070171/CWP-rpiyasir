#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    print(list(range(first, second + 1)))

# วิธีรันบน Linux:
#   chmod +x free_range.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./free_range.py | cat -e
#   ./free_range.py 10 14 | cat -e
