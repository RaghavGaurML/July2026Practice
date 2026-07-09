users = [{"id": 1, "name": "Asha", "age": 25, "active": True}, 
         {"id": 2, "name": "Bob", "age": 30, "active": False}, 
         {"id": 3, "name": "Cathy", "age": 41, "active": True}]

activeUserNames = [u["name"] for u in users if u["active"] == True]
under35UserNames = [u["name"] for u in users if u["age"] <= 35]

under35AndActiveUserNamesI = set(activeUserNames).intersection(set(under35UserNames))
under35AndActiveUserNamesII = [u["name"] for u in users if u["age"] <= 35 and u["active"] == True]

print(activeUserNames)
print(under35UserNames)
print(under35AndActiveUserNamesI)
print(under35AndActiveUserNamesII)

firstUserName = users[0].get("name")
firstUserProfession = users[0].get("profession", None)

print(firstUserName)
print(firstUserProfession)

firstUserInfo = users[0].items()
firstUserKeys = users[0].keys()
firstUserValues = users[0].values()

print(firstUserInfo)
print(firstUserKeys)
print(firstUserValues)