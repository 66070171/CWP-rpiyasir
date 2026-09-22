#!/usr/bin/env python3

def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

# วิธีรันบน Linux:
#   chmod +x family_affairs.py   <- ทำครั้งเดียว ให้ไฟล์รันได้
#
#   ตัวอย่างทั้งหมดจากโจทย์:
#   ./family_affairs.py
