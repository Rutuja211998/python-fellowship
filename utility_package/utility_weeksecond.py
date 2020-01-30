"""
This is a utility_secondweek file which contains Node and LinkedList class which having different methods.
Also here we write method for Unordered list, Ordered list and Prime Two D-array, Prime Anagram questions.

Author: Rutuja Tikhile.
Date: 21/01/2020.
"""
from utility_package.utility_firstweek import Utility


class Node:
    """
    This is the node class, nodes are created by implementing a class
    which will hold the pointers along with the data element.
    Class contains the definition to create an object instance.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


####################################################################################################


class LinkedList:
    """"
    This is the LinkedList class, A linked list is a sequence of data elements,
    which are connected together via links. Each data element contains
    a connection to another data element in form of a pointer.
    In this class we made different methods to perform mentioned task.
    """

    def __init__(self):
        self.head = None

    def display(self):  # to display the linked list.
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def add(self, data):  # to add the data in the linked list.

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node

    def insert(self, data):  # to insert data at the end.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):  # remove from yhe position.
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node
            current_node = current_node.next
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def search(self, data):  # It returns match object.
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def sort(self, item):  # sort the data from list as ascending order.
        current = self.head
        previous = None

        while current is not None:
            if current.data > item:
                break
            previous, current = current, current.next

        new_node = Node(item)
        if previous is None:
            new_node.next, self.head = self.head, new_node
        else:
            new_node.next, previous.next = current, new_node


################################################################################################


class UnorderedList:

    def __init__(self):
        """
        Creating object of linked list for maintain and store data.
        """
        self.list = LinkedList()

    def unorderedList(self):
        """
            Read data from file and store in linked list for this we use
            open () function in Python to open a file in read or write mode.
            Take one input from user and search in linked list
            If data found in linked list then remove that data from linked list
            If not found then add that data into linked list.
        """
        file = open("text_fromafile.txt", 'r')  # open to open the file which is already created in the
        # data structure package and "r" is used for reading file.
        for word in file:
            word_line = word.split()
            for element in word_line:
                self.list.add(element)  # to add elements.
        self.list.display()  # calling display function to display file.
        print()
        a = input("Enter a word to search : ").strip()
        if self.list.search(a):  # to search word in the list.
            print("found")
            self.list.remove(a)  # to remove the searched word in the list.
        else:
            print("Not found")
            self.list.add(a)
        return self.list.display()


##############################################################################################


class OrderedList:
    def __init__(self):
        """
            Creating object of linked list for maintaining data.
        """
        self.list = LinkedList()

    def orderList(self):
        """
            Read data from file and store in sorted order in linked list for this
            we use open () function in Python to open a file in read or write mode.
            Take one input from user and search in linked list
            If data found in linked list then remove that data from linked list
            If not found then add that data into linked list.
        """
        file = open("number_fromafile.txt", 'r')  # open to open the file which is already created in the
        # data structure package and "r" is used for reading file.
        for number in file:
            num_line = number.split()
            for element in num_line:
                self.list.sort(int(element))  # to sort the numbers in ascending order in the number file.
        self.list.display()  # calling display function to display file.
        print()
        a = int(input("Enter a number to search : "))
        if self.list.search(a):  # to search word in the list.
            print("found")
            self.list.remove(a)  # to remove the searched word in the list.
        else:
            print("Not found")
            self.list.sort(a)
        self.list.display()


#############################################################################################


class PrimeTwoDArray:
    @staticmethod
    def prime_two_d():
        """
        In this method Take a range of 0 - 1000 Numbers and find the Prime numbers
        in that range. Store the prime numbers in a 2D Array, the first dimension
        represents the range 0-100, 100-200, and so on. While the second dimension
        represents the prime numbers in that range.

        :return:Print prime numbers in two d array.
        """
        a = Utility()

        array_prime = []  # array for storing the whole list.
        lower = 0
        upper = 100
        while True:
            list = []  # array for storing small list i.e up to 100.
            for num in range(lower, upper+1):
                a = Utility.is_prime(num)
                if a is True:
                    list.append(num)
                if a >= upper-1:
                    break
            array_prime.append(list)
            lower = upper
            upper = upper + 100
            if upper >= 1001:
                break
        return array_prime
###############################################################################################

    # PRIME ANAGRAM

    """
    This is the Prime Number Program that store only the numbers in that range that
    are Anagrams. For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
    Further store in a 2D Array the numbers that are Anagram and numbers that are not Anagram

    """
    @staticmethod
    def primes(n):  # it returns list of prime numbers from 0 to 1000.
        list = []
        for num in range(0, 1000):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        return list

    @staticmethod
    def anagram(a):  # it gives anagrams.
        # initialize a list
        anagram_list = []
        for i in a:
            for j in a:
                if i != j and (sorted(str(i)) == sorted(str(j))):
                    anagram_list.append(i)
        return anagram_list

#####################################################################################################


