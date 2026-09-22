#!/usr/bin/env python3

import sys

print("Number of parameters:", len(sys.argv) - 1, end=".\n")

# วิธีรันบน Linux:
#   chmod +x parameters.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./parameters.py
#   ./parameters.py "initiation"
#   ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
