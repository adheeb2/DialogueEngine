import json
# When s is used in the ends of load or dump, we know it consist of string either in input or output part(converting to string or reverse)
# when no s is used, it is for converting to file or reverse
data = {"name":"adheeb",
"age":12,
"foods":["apple","banana","orange"]}

json_string = json.dumps(data,indent=2)#dumps convert dict into json string, indent is just used for readability    
print(json_string)
person = json.loads(json_string)#loads JSON string into a Python object(dict/list)
print(person["foods"][0])

