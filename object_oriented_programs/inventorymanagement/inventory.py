"""
Overview :
This is the inventory file which contains class named Inventory.
Purpose :
Json concept, reading json data and print.
Author: Rutuja Tikhile.
Date: 29/01/2020
"""
import json


class Inventory:

    def __init__(self):
        pass

    @staticmethod
    def inventory():
        """ Method to print json data into python string
        :return: inventory_dict : dictionary of inventory
        """
        try:
            # opening the inventory file
            with open("/home/admin1/PycharmProjects/Fellowship/Json_files/inventory_mng.json") as file:
                inventory_dict = json.load(file)
            # traversing dictionary to print the values
            for key in inventory_dict:
                for value in inventory_dict[key]:
                    print(key)
                    price = 0
                    weight = 0
                    price += int(value["price"])
                    weight += int(value["weight"])
                    print("Name:", value["name"])
                    print("Price:", value["price"])
                    print("Weight:", value["weight"])
                    print()
            return inventory_dict
        except FileNotFoundError:
            print("File not found!!!")
        except Exception:
            print("Error")


if __name__ == '__main__':
    Inventory.inventory()