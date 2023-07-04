import xml.etree.ElementTree as ET
import json

tree= ET.parse('outuser.xml')
print(type(tree))
root= tree.getroot()
print(root)
for i in root:
    print(i.tag)
data = root.find('id')
print(data)

print("-------------")
print(root.findall("address"))
print("-------------")
print(root.find('address'))
# root.find('id').text=23
print(root.find('id').text)
addresss=root.findall("address")
# for i in addresss:
#     for item in i:
#         print(item.text)
for i in root.iter():
    print(i.tag,i.text)

import xml.dom.minidom as MD

data1=MD.parse('outuser.xml')
# for i in data1.getElementsByTagName('*'):
#     print(i.tagName)
print("-------------")
for i in data1.childNodes:
    # print(i.childNodes[0].nodeName)
    # print(i.childNodes[0].childNodes[0].data)
    print(i.childNodes[0].childNodes)

import xmltodict

with open('outuser.xml','r') as file:
    data2=file.read()
datadict=xmltodict.parse(data2)
print(datadict)

with open('outuser3.json','w') as file:
    json.dump(datadict['root'],fp=file,indent=4,default=str)