# type of dictionary in which we define the data types of KEYS
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person={'name':'Anas','age':'21'} # age should be string but it doesnt throw error if we write it as string i.e there is no validation
print(new_person)