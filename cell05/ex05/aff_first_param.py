#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")

# วิธีรันบน Linux:
#   chmod +x aff_first_param.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./aff_first_param.py | cat -e
#   ./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
