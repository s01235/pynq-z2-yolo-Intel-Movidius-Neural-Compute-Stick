import os

xml_dir="C:\\Users\\ASUS\\Desktop\\temp\\有害垃圾"

image_dir = "C:\\Users\\ASUS\\Desktop\\temp1\\有害垃圾"
xmlfiles=os.listdir(xml_dir)
image_files = os.listdir(image_dir)

names = []

for xmlfile in xmlfiles:
    names.append(xmlfile[:-4])

for image_file in image_files:
    if image_file[:-4] not in names:
        os.remove(image_dir + "\\" + image_file)
