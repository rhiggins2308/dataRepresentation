import json

data = {
    'name' : 'joe',
    'age' : 21,
    "student" : True
}

# print(data)

# file = open("simple.json", 'w')
# json.dump(file, data)

with open('simple.json', 'w') as f:
    json.dump(data, f, indent=4)