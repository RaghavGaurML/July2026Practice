from core_data_structures import users

# package code into functions
def get_active_users_under_age(users: list[dict], age: int) -> list[dict]:
    return [u for u in users if u["age"] <= age and u["active"]]

def get_user_by_id(users: list[dict], user_id: int) -> dict | None:
    return next((u for u in users if u["id"] == user_id), None)

def group_names_by_status(users: list[dict]) -> dict:
    user_status = {"active": [u["name"] for u in users if u["active"]], 
                   "not_active": [u["name"] for u in users if not u["active"]]}
    
    return user_status

def get_average_user_age(users: list[dict]) -> float:
    sum_ages = 0

    for u in users:
        sum_ages += u["age"]

    return round(sum_ages/len(users), 2)


print(get_active_users_under_age(users, 35))
print(get_user_by_id(users, 2))
print(get_user_by_id(users, 99))
print(group_names_by_status(users))
print(get_average_user_age(users))