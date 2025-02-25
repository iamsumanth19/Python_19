import json

data={"name":"sumanth","age":21,"adress":{"village":"yemmiganur","district":"kurnool","pincode":518360}}

json_data=json.dumps(data,indent=4)

print(json_data)

json_python_data=json.loads(json_data)

print(json_python_data)