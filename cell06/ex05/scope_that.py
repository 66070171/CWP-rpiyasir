#!/usr/bin/env python3

def add_one(number):
    number = number + 1
    print("Inside the method:", number)

my_number = 42

print(my_number)
add_one(my_number)
print(my_number)

# สิ่งที่สังเกตได้ (What do you observe?):
#   my_number ยังเป็น 42 เท่าเดิม ไม่ได้กลายเป็น 43
#   เพราะ number ในฟังก์ชันเป็นตัวแปรคนละตัวกับ my_number ข้างนอก
#   เป็นแค่สำเนาของค่า การแก้ค่าข้างในจึงไม่กระทบตัวแปรข้างนอก
#   (เรียกว่าเรื่อง scope ของตัวแปร)

# วิธีรันบน Linux:
#   chmod +x scope_that.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./scope_that.py
