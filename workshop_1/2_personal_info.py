#!/usr/bin/python3

import os


class User():
    """User class representation"""
    data = ()

    def __init__(self, name, lastname, profession, age, city, phone, email):
        """Initialize attributes"""
        self.name = name
        self.lastname = lastname
        self.profession = profession
        self.age = age
        self.city = city
        self.phone = phone
        self.email = email

    def store_into_tuple(self):
        """Store the object information into the tuple."""
        User.data = User.data + (self,)

    def list_of_dictionaries(self, tuple_info):
        """Show the information through of dictionaries"""
        final_list = []

        for i in range(len(tuple_info)):
            inf_dict = {}

            inf_dict = {
                'name': tuple_info[i].name,
                'lastname': tuple_info[i].lastname,
                'profession': tuple_info[i].profession,
                'age': tuple_info[i].age,
                'city': tuple_info[i].city,
                'phone': tuple_info[i].phone,
                'email': tuple_info[i].email
            }
            final_list.append(inf_dict)

        return final_list


if __name__ == '__main__':
    for i in range(1, 3):
        usr = "User " + str(i)
        print(f"Please complete the information: [{usr}]\n")

        # Get user information
        name = str(input("Name: "))
        lastname = str(input("Lastname: "))
        profession = str(input("Profession: "))
        age = str(input("Age: "))
        city = str(input("City: "))
        phone = str(input("Phone: "))
        email = str(input("Email: "))

        # Create user instances
        obj = User(name, lastname, profession, age, city, phone, email)
        obj.store_into_tuple()
        os.system("clear")

    tuple_info = obj.data
    # print(tuple_info)

    res = obj.list_of_dictionaries(tuple_info)
    print(f"Data representation as list of dictionaries:\n\n{res}")
