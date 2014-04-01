import json

data = {}

with open("input2.json") as fh:
    for item in json.load(fh):
        item["loss"] = 0
        item["selected"] = False
        data[item["name"]] = item

for name, item in data.items():
    boss = item["boss"]

    if boss == None:
        continue
    
    boss = data[boss]
    boss["loss"] += item["party-animal-score"]

for name, item in data.items():
    item["value"] = item["party-animal-score"] - abs(item["loss"])

for name, item in sorted(data.items(), key=lambda (key, val): val["value"], reverse=True):
    if item["value"] < 1:
        break

    boss = item["boss"]

    if boss == None:
        continue
        
    if data[boss]["selected"]:
        continue

    item["selected"] = True
    print name
