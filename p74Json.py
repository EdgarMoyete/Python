# codificar: json.dumps: python a json
# decodificar: json.loads: json a python

import json

# json a python
# json
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse
y = json.loads(x)
print(y["age"])
print(type(x))
print(type(y))

# python a json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convertir a JSON
y = json.dumps(x)
print(type(x))
print(type(y))