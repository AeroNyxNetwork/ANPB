import json

f =open("./ANPBDemo.json", "r")
json_obj = json.loads(f.read())
for i in range(5000):
    f = open(f"{i+1}.json", "w")
    json_obj["name"] = f"ANPB #{i+1}"
    f.write(json.dumps(json_obj))

print(json_obj)