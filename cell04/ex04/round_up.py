#!/usr/bin/env python3

import math

num = float(input("Give me a number: "))

print(math.ceil(num))

# วิธีรันบน Linux:
#   chmod +x round_up.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./round_up.py    (พิมพ์ 41.42)
#   ./round_up.py    (พิมพ์ 42)
#   ./round_up.py    (พิมพ์ 0.001)
