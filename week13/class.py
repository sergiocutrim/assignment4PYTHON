# dictionary
friend = {"name": "Smith", "email": "smith@example.com", "phone": "123-2938"}
# print(friend)
# print(type(friend))
# print(len(friend))
# print(friend["name"])
# print(friend["email"])
# print(friend["phone"])
# print(friend["location"])

#print(friend.get("name"))  # friend["name"]
#print(friend.get("location"))  # None
#print(friend.get("location", "Unknown location"))  # Unknown location
#print(friend.get("email", "No email"))  # smith@example.com


# adding and updating elements in dictionary
login = {"name": "Scott", "email": "newemail@example.com", "loginDate": "2030-01-01 10:30"}
#print(login)
#login["email"] = "newemail@example.com"  # update element
#print(login)
#login["phone"] = "123-23893"  # adding elements
#print(login)
#login.update({"email": "againchanged@example.com", "phone": "123-123", "amount": 10000})
#print(login)



# removing elements in dictionary
user = {"email": "john@test.com", "password": "john123", "phone": "1234", "age": 20}
print(user)
print(user.pop("password"))  # john123
print(user)
print(user.popitem())  # returns ('phone', '1234')
print(user)
# print(user.pop("city"))  # KeyError: 'city'
# print(user)

del user["phone"]  # removes a specific key
print(user)

user.clear()  # removes all elements
print(user)

del user
# print(user)   # NameError: name 'user' is not defined
--

# copy dictionary
user1 = {"username": "John", "age": 22}
# user2 = user1  # copy reference
# user2 = user1.copy()  # create a new dictionary object and copy all elements
# user2 = dict(user1)  # create a new dictionary object and copy all elements
user2 = {**user1}  # kwargs operator
user2["age"] = 25
print(user1)
print(user2)