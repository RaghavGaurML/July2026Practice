users = [{"id": 1, "name": "Asha", "age": 25, "active": True}, 
         {"id": 2, "name": "Bob", "age": 30, "active": False}, 
         {"id": 3, "name": "Cathy", "age": 41, "active": True}]

active_user_names = [u["name"] for u in users if u["active"]]
under_35_user_names = [u["name"] for u in users if u["age"] <= 35]

under_35_and_active_user_names_I = set(active_user_names).intersection(set(under_35_user_names))
under_35_and_active_user_names_II = [u["name"] for u in users if u["age"] <= 35 and u["active"] == True]

print(active_user_names)
print(under_35_user_names)
print(under_35_and_active_user_names_I)
print(under_35_and_active_user_names_II)

first_user_name = users[0].get("name")
first_user_profession = users[0].get("profession", None)

print(first_user_name)
print(first_user_profession)

first_user_info = users[0].items()
first_user_keys = users[0].keys()
first_user_values = users[0].values()

print(first_user_info)
print(first_user_keys)
print(first_user_values)