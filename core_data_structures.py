users = [{"id": 1, "name": "Asha", "age": 25, "active": True}, 
         {"id": 2, "name": "Bob", "age": 30, "active": False}, 
         {"id": 3, "name": "Cathy", "age": 41, "active": True}]


# Basic list manipulation
active_user_names = [u["name"] for u in users if u["active"]]
under_35_user_names = [u["name"] for u in users if u["age"] <= 35]

# Using sets vs list manipulation
under_35_and_active_user_names_I = set(active_user_names).intersection(set(under_35_user_names))
under_35_and_active_user_names_II = [u["name"] for u in users if u["age"] <= 35 and u["active"]]

print(active_user_names)
print(under_35_user_names)
print(under_35_and_active_user_names_I)
print(under_35_and_active_user_names_II)

# Using get
first_user_name = users[0].get("name")
first_user_profession = users[0].get("profession", None)

print(first_user_name)
print(first_user_profession)

# Dict functions
first_user_info = users[0].items()
first_user_keys = users[0].keys()
first_user_values = users[0].values()

print(first_user_info)
print(first_user_keys)
print(first_user_values)

# Dict lookup by id
user_1 = [u for u in users if u["id"] == 1]
print(user_1)

# using next
user_2 = next((u for u in users if u["id"] == 2), None)
print(user_2)


users_by_id = {u["id"]: u for u in users}
print(users_by_id[2]["name"])

# Count active users
active_users = 0 

for u in users:
    if u["active"]:
        active_users += 1

print(active_users)

# alternative approach
# active_users = sum(1 for u in users if u["active"])

# Sort users by age
users_by_age = sorted(users, key = lambda x : x["age"])
print(users_by_age)

# Group names by active status
status = {"active": [], "not active": []}

for u in users:
    if u["active"]:
        status["active"].append(u["name"])
    else:
        status["not active"].append(u["name"])

print(status)


