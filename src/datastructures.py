
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import json

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        memberOne = {
            "id": 1,
            "name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }

        memberTwo = {
            "id": 2,
            "name": "Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        }

        memberthree = {
            "id": 3,
            "name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers": [1]
        }        

        # example list of members
        self._members = [memberOne,memberTwo,memberthree]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_member = { 
            "id": self._generateId(),
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member);
        return new_member

    def delete_member(self, id):
        #ill this method and update the return
        
        pass

    def get_member(self, id):                
        for member_obj in self._members: # recorriendo el arreglo
            # logica sobre un member
            if(member_obj["id"] == id):
                return member_obj # regresando el member encontrado

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    


