#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")

# วิธีรันบน Linux:
#   chmod +x upcase_it.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./upcase_it.py | cat -e
#   ./upcase_it.py "initiation" | cat -e
#   ./upcase_it.py 'This exercise is quite easy!' | cat -e
