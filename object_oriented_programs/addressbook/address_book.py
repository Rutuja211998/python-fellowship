"""
Overview:
To maintain address book.
Purpose:
For showing list to user.
Author: Rutuja Tikhile
Date: 29/01/2020
"""
from object_oriented_programs.addressbook.service import Service


class AddressBook:
    def __init__(self):
        """
        This is the address book method in which we are using services.
        """
        self.obj = Service()

    def address_book(self):
        """

        :return:
        """
        try:
            while True:
                print("**********************")
                print("1.Create\n2.Open\n3.Save\n4.Save as\n5.Add person\n6.Delete Person\n7.Edit person\n8.Quit")
                choice_selected = int(input("Select any choice: "))
                if choice_selected == 8:
                    self.obj.save()
                    print("Exited")
                    return
                elif choice_selected > 8:
                    print("You have selected wrong choice: ")
                    continue
                choice = {1: "Create", 2: "Open", 3: "save", 4: "save as", 5: "add_person", 6: "delete_person", 7: "edit_person"}
                fun = getattr(self.obj, choice[choice_selected])
                fun()
        except Exception:
            print("You have enter wrong input!!")
            self.address_book()


if __name__ == "__main__":
    obj = AddressBook()
    obj.address_book()