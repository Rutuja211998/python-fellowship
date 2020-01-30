"""
Overview :
This is the inventorymng file which contains class named InventoryManagement.
Purpose :
Json concept, reading json data and print.
Author: Rutuja Tikhile.
Date: 27/01/2020
"""
import json


class InventoryManager:

    def __init__(self, json_file):  # Taking file to get data from json file
        self.json_file = json_file
        self.inventory = None

    def inventory_factory(self):
        """
        This is the method to get data from inventory file and show value of each item in inventory.
        """

        with open(self.json_file, 'r') as file:
            self.inventory = json.load(file)
        # for item in self.inventory["inventory"]:
        #     print("Adding data into json file.")
            # print(data_serialized = json.dump(inventory, open('inv_management.json', "r"), indent=4))
            # print(file, "value of {item['weight']}Kg of {item['name']} is {item['weight'] * item['price_per_kg']}")

    def add_to_inventory(self):
        """
        Method to add item to inventory and save to json file
        """
        n = int(input("Enter number of items to add in inventory :\n"))
        for i in range(n):
            while True:
                try:  # Getting information about data to add to inventory json file
                    item = input("Item name would want to enter in inventory :\n")
                    weight = int(input("Enter weight of the product you are adding to inventory :\n"))
                    price = int(input("Enter cost per kg of the product "))

                except ValueError:
                    print("Please enter values for weight and price per kg")

                else:
                    break

            with open(self.json_file, 'r+') as file:  # Saving changes to json file
                data = dict()
                data['name'] = item
                data['weight'] = weight
                data['price_per_kg'] = price
                self.inventory["inventory"].append(data)
                json.dump(self.inventory, file, indent=4)


if __name__ == "__main__":
    obj = InventoryManager("inv_management.json")
    obj.inventory_factory()
    obj.add_to_inventory()
