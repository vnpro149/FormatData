import json
import xmltodict

# with open('user.json','r') as file:
#     data=file.read()

# print(type(data))
# datajson=json.loads(data)
# print(datajson,type(datajson))

with open('user.json','r')as f:
    data1= json.load(f)
print(data1,type(data1))
datajson={'root':data1}
dataxml=xmltodict.unparse(datajson)
print(dataxml,type(dataxml))
with open("outuser.xml",'w') as file:
    file.write(dataxml)