import json
import pprint

data = {"state": "bad", "activity": "zzz", "speech": "łałałiła", "eqiupped": None}

# json.dumps() wrzuca dane do formatu json (postać stringowa), "s" na końcu od "string"
jsondata = json.dumps(data, ensure_ascii=False)
# ensure_ascii=False     dba o polskie znaki
print("encoded:", jsondata)

jsondata2 = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
print(jsondata2)

with open("jsondata.json", "w", encoding="UTF-8") as file:
    json.dump(data, file, ensure_ascii=False)

# dekodowanie formatu json
print("decoded:", json.loads(jsondata))

with open("jsondata.json", encoding="UTF-8") as file:
    print("encoded from file:", file.read())
    file.seek(0)
    print("decoded from file:", json.load(file), "\n")


pprint.pprint(jsondata)
pprint.pprint(jsondata2)
