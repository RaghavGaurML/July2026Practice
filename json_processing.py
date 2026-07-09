import json

def read_json(json_name : str) -> list | None:
    try:
        with open(json_name, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found, please use an existing json")
    except json.JSONDecodeError:
        print("Decode error, the file is malformed")

    return None

data = read_json("practice_user_jsons/users_good.json")
print(data)

data = read_json("practice_user_jsons/users_okay.json")
print(data)

data = read_json("practice_user_jsons/users_bad.json")
print(data)

