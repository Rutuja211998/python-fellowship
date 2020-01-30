"""
Overview :
This is the datamng file which contains class named DataManagement.
Purpose :
Json concept, reading json data and print.
Author: Rutuja Tikhile.
Date: 27/01/2020
"""
import json


class DataManagement:
    def __init__(self):
        """
        Loading data from the Json file(read-write).
        Print price and data from inventory.
        Calculate the value for every Inventory.
        """
        file = open("/home/admin1/PycharmProjects/Fellowship/Json_files/data_mng.json", "r")  # reading file
        data = json.load(file)
        # print(data)
        data_serialized = json.dump(data, open('data_mng.json', "w"), indent=4)  # writing file

        for key in data:
            for value in data[key]:
                price = 0
                weight = 0
                price += int(value["price"])
                weight += int(value["weight"])
                print("Name:", value["name"])
                print("Weight:", value["weight"])
                print("Price:", value["price"])
                print("total price for 10kg:", price * weight)
                print()