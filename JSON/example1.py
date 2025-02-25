import json

data={'name': 'sumanth', 'age': 21, 'adress': {'village': 'yemmiganur', 'district': 'kurnool', 'pincode': 518360}}

with open("adress.json","w") as json_file:
    json.dump(data,json_file,indent=4)

print(json_file)

with open('adress.json',"r") as json_file:
    json_data=json.load(json_file)

print(json_data)