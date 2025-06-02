import pprint

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "cycling", "chess"],
    "details": {
        "height": 165,
        "weight": 60,
        "address": {"city": "Beijing", "zipcode": "100000"},
    },
}

formatted = pprint.pformat(data)
print("formatted date:\n" + formatted)
print(type(formatted))
