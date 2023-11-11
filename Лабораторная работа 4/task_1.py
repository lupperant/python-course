import json

filename = "input.json"


def task() -> float:
    result = 0
    with open(filename) as file:
        data = json.load(file)
    for i in data:
        result += i["score"] * i["weight"]
    return round(result, 3)


print(task())
