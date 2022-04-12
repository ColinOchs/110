#dictionaries


from audioop import add


def test_dict():
    me = {
        "first": "Colin",
        "last": "Ochs",
        "age": 39,
        "hobbies": [],
        "address": {
            "street": "East End",
            "city": "Colombia"
        }
    }

    print(me["first"] + " " + me["last"])

    #  wont work--->print("my age is: " + me["age"])
    print("my age is: " + str(me["age"]))
    print(f"my age is: {me['age']}")

    address = me["address"]
    print(type(address))
    print(address)
    print(address["street"])

    print(me["address"]["city"])
#add new keys
    me["color"] = "red"

#modify existing keys
    me["age"] = 36
#check if a key exist in dictionary
    if "age" in me:
        print("age exists")

print("----------dictionary test-----------")
test_dict()