"""
This is the stock_mng file which contains class named StockManagement.
Purpose :
Json concept, reading json data and print.
Author: Rutuja Tikhile.
Date: 27/01/2020
"""
import json


class StockManagement:
    def __init__(self):
        """
        Loading data from the Json file(read-write).
        Print price and data from inventory.
        Calculate the value for every Inventory.
        """
        try:
            file = open("/home/admin1/PycharmProjects/Fellowship/Json_files/stock_acc.json", "r")  # reading file
            data = json.load(file)
            print(data)

            data_serialized = json.dump(data, open('stock_acc.json', "w"), indent=4)  # writing file
            print(data_serialized)
            for key in data:
                for value in data[key]:
                    print(key)
                    no_of_share = 0
                    price = 0
                    no_of_share += int(value["no_of_share"])
                    price += int(value["price"])
                    print("Name:", value["name"])
                    print("No_of_share:", value["no_of_share"])
                    print("Price:", value["price"])
                    print("total price:", price * no_of_share)
                    print()

        except Exception:
            print("file not found!!")


if __name__ == "__main__":
    StockManagement()