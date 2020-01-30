"""
Overview :
This is the inventorymng file which contains class named InventoryManagement.
Purpose :
Json concept, reading json data and print.
Author: Rutuja Tikhile.
Date: 27/01/2020
"""
import json


class InventoryManagement:
    def __init__(self):
        """
        Extend the above program to Create InventoryManager to manage the Inventory.
        The Inventory Manager will use InventoryFactory to create Inventory Object from JSON.
        The InventoryManager will call each Inventory Object in its list to calculate the Inventory Price
        and then call the Inventory Object to return the JSON String.
        """
        file = open("/home/admin1/PycharmProjects/Fellowship/Json_files/data_mng.json", "r")
        data = json.load(file)

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