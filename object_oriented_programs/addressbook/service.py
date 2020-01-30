"""
Overview:
Provide different services to address book.
Purpose:
Creating different service.
Author: Rutuja Tikhile
Date: 29/01/2020
"""
import json
from re import search


class Service:

    def __init__(self):
        self.person_data = []
        self.file_name = None

    def create(self):
        """
        Creating new json file.
        :return:
        """
        try:
            file_name = input("Enter file name for creating new json file: ").strip()
            if search("[a-zA-Z]", file_name) is not None:
                f = open(file_name + ".json", 'w+')
                f.close()
            else:
                raise ValueError
        except ValueError:
            print("File name should be alphabet only")

    def open(self):
        """
        Open json file and read json data from json file
        :return:
        """
        file_name = input("Enter file name: ").strip().lower()
        try:
            with open(file_name + ".json") as data:
                self.person_data = json.load(data)
                self.file_name = file_name
        except Exception:
            print("file not found!!")

    def save(self):
        """
        Save json data in to json file.
        :return:
        """
        try:
            with open(self.file_name + ".json", 'w') as data:
                json.dump(self.person_data, data)
                data.close()
        except Exception:
            print("you have not open any file!!")

    def save_as(self):
        """
        save as the json data in to json file.
        :return:
        """
        file_name = input("Enter file name with extension json: ").strip()
        json_pattern = search("\.json", file_name)
        if json_pattern is not None and json_pattern.group() == ".json":
            select = 1
        else:
            print("You enter wrong file extension")
            return
        with open(file_name, 'w+') as data:
            if select == 1:
                json.dump(self.person_data, data)

    def add_person(self):
        """
        Creating new person data and add them.
        :return:
        """
        try:
            first_name = input("Enter first name: ").strip().upper()
            last_name = input("Enter last name: ").strip().upper()
            address = input("Enter address: ").strip().upper()
            city_name = input("Enter city name: ").strip().upper()
            state_name = input("Enter state name: ").strip().upper()
            zip_code = input("Enter zip code: ").strip()
            phone_number = input("Enter phone number: ").strip()
            if not first_name.isalpha() and not last_name.isalpha() and not address.isalpha() and not city_name.isalpha() and not state_name.isalpha() and not zip_code.isalpha() and not phone_number.isalpha():
                raise ValueError
        except ValueError:
            print("You have to entered correctly!!")

        else:
            new_person = {"data": {}}

            new_person["data"]["address"] = address
            new_person["data"]["city_name"] = city_name
            new_person["data"]["state_name"] = state_name
            new_person["data"]["zip_code"] = zip_code
            new_person["data"]["phone_number"] = phone_number
            new_person["first_name"] = first_name
            new_person["last_name"] = last_name
            flag = True
            for i in self.person_data:
                if i["first_name"] == first_name and i["last_name"] == last_name:
                    print("This data is duplicate")
                    flag = False
                    break
            if flag:
                self.person_data.append(new_person)
            print(self.person_data)

    def delete_person(self):
        """
        Take two input from user first name and last name and then delete
        the data from list.
        :return:
        """
        try:
            first_name = input("Enter first name: ").strip().upper()
            last_name = input("Enter last name: ").strip().upper()
            if not first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have to enter in alphabet")

        else:
            for i in range(len(self.person_data)):
                if self.person_data[i]["first_name"] == first_name and self.person_data[i]["last_name"] == last_name:
                    self.person_data.remove(self.person_data[i])
                    print("Data deleted")
                    break

    def edit_person(self):
        """
        Taking two input from the user and check weather it available or not.
        edit the information of person.
        :return:
        """
        try:
            first_name = input("Enter first name: ").strip().upper()
            last_name = input("Enter last name: ").strip().upper()
            if not first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have to enter name in alphabet")
        else:
            flag = True
            for i in range(len(self.person_data)):
                if self.person_data[i]["first_name"] == first_name and self.person_data[i]["last_name"] == last_name:
                    flag = False
                    while True:
                        choice = int(input("\t1.First name\n\t2.Last name\n\t3.Address\n\t4.City name\n\t5.State name\
                        \n\t6.Zip code\n\t7.Phone number\n\t8.Nothing wants to change.\nEnter choice: "))
                        if choice == 1:
                            first = input("Enter first name:").strip().upper()
                            if not first.isalpha():
                                print("You have to enter first name in alphabet.")
                            else:
                                self.person_data[i]["first_name"] = first
                        elif choice == 2:
                            last = input("Enter last name:").strip().upper()
                            if not last.isalpha():
                                print("You have to enter last name in alphabet.")
                            else:
                                self.person_data[i]["last_name"] = last
                        elif choice == 3:
                            addr = input("Enter address:").strip().upper()
                            self.person_data[i]["address"] = addr
                        elif choice == 4:
                            city = input("Enter city name:").strip().upper()
                            if not city.isalpha():
                                print("You have to enter city name in alphabet.")
                            else:
                                self.person_data[i]["city_name"] = city
                        elif choice == 5:
                            state = input("Enter state name:").strip().upper()
                            if not state.isalpha():
                                print("You have to enter state name in alphabet.")
                            else:
                                self.person_data[i]["state_name"] = state
                        elif choice == 6:
                            zip = input("Enter zip code:").strip()
                            if not zip.isnumeric() and len(zip) != 6:
                                print("You have to enter zip code in numeric and length must be 6")
                            else:
                                self.person_data[i]["zip_code"] = zip
                        elif choice == 7:
                            number = input("Enter phone number:").strip()
                            if not number.isnumeric() and len(number) == 10:
                                print("You have to enter phone number in numeric and length must be 10")
                            else:
                                self.person_data[i]["phone_number"] = number
                        elif choice == 8:
                            return
                        else:
                            print("You selected wrong choice")

            if flag:
                print("Data not available")













