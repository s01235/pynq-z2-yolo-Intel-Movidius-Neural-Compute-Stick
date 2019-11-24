import xml.etree.ElementTree as ET
import os
import sys

xml_dir = "C:\\Users\\ASUS\\Desktop\\Annotations"

xml_files = os.listdir(xml_dir)

num = 0

for xml_file in xml_files:
    num = num + 1
    tree = ET.parse(xml_dir + "\\"+ xml_file)
    root = tree.getroot()
    obj = root.find("object")
    name = obj.find("name")
    if (name.text == "有害垃圾"):
        name.text = "Harmful"
    elif (name.text == "厨余垃圾"):
        name.text = "Kitchen "
    elif (name.text == "其他垃圾"):
        name.text = "Other"
    elif (name.text == "可回收物"):
        name.text = "Recyclable "
    tree.write(xml_dir + "\\"+ xml_file, encoding="utf-8")

print(num)
