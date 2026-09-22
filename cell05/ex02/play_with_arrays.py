#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = []

for n in numbers:
    if n > 5:
        new_numbers.append(n + 2)

print(numbers)
print(new_numbers)

# วิธีรันบน Linux:
#   chmod +x play_with_arrays.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./play_with_arrays.py | cat -e
