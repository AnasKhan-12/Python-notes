person={"name":"Anas","age":24,"city":"Lahore"}

# print(person.get("age"))

person.update({"Gender" : "Male"})
#person.pop("age")
#person.popitem()
#person.clear
print(person.keys())

for key,value in person.items():
    print(key,value)