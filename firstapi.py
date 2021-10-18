import json

filedata = '{"fruit": "Apple","size": "Large","color": "Red"}'

data = json.loads(filedata)
print(type(data))
print(data)

print(data["size"])

