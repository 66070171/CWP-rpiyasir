#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)

# วิธีรันบน Linux:
#   chmod +x scan_it.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./scan_it.py | cat -e
#   ./scan_it.py "the" | cat -e
#   ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
