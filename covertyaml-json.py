from ruamel import yaml
import json

with open('user.yaml','r') as file:
    data= yaml.safe_load(file)
# print(data)
# print(type(data))
# with open('user.yaml','r') as file:
#     data1=yaml.load(file,Loader=yaml.RoundTripLoader)
# print(data1)
# print(type(data1))
# for i in data:
#     print(i)
#     print(data[i])
# print("id",data['id'])
for key,value in data.items():
    print(key,value)

# datajson=json.dumps(data,indent=4,default=str)
# print(datajson)
# print(type(datajson))
# with open('outuser.json','w') as file:
#     file.write(datajson)

with open('outuser1.json','w') as file:
    json.dump(data,fp=file,indent=4,default=str)