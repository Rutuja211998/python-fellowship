"""
This is the file in which we runs the program.
Author:Rutuja Tikhile.
Date: 25/01/2020.
"""
from utility_package.utility_secondweek import Stack
from utility_package.utility_weeksecond import LinkedList

# llist = Stack()
#
# llist.push(10)
# llist.push(20)
# llist.push(30)
# llist.pop()

llist = LinkedList()
llist.add(20)
llist.add(30)
# llist.pop_first()
llist.insert(40)
print(llist.search(50))

# llist.remove("2")
# print(llist.search("1"))

# llist.stack.display()
llist.display()
