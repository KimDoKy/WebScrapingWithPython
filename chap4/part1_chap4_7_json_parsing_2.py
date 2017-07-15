import json

jsonString = '{"arrayofNums":[{"number":0},{"number":1},{"number":2}],"arrayofFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayofNums"))
print(jsonObj.get("arrayofNums")[1])
print(jsonObj.get("arrayofNums")[1].get("number")+jsonObj.get("arrayofNums")[2].get("number"))
print(jsonObj.get("arrayofFruits")[2].get("fruit"))
