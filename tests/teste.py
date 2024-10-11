import json

with open ('teste.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
print(data)
    
for i in data:
    print(data[i]["titulo"])
    print(data[i]["tipo"])
    for j in data[i]["genero"]:
        print(j)
    print(data[i]["status"])
    