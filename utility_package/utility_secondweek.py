"""
This is a utility_secondweek file which contains Node, LinkedList class, stack class, QUEUE and DeQueue
having different methods to perform BalancedParentheses and PalindromeChecker, Reverse Anagram, Binary search tree task.
Author: Rutuja Tikhile.
Date: 22/01/2020.
"""


class Node:
    """
    This is the node class, nodes are created by implementing a class
    which will hold the pointers along with the data element.
    Class contains the definition to create an object instance.
    """

    def __init__(self, obj):  # this class creates node.
        self.next = None
        self.object = obj

##########################################################################################


class LinkedList:
    """"
    This is the LinkedList class, A linked list is a sequence of data elements,
    which are connected together via links. Each data element contains
    a connection to another data element in form of a pointer.
    In this class we made different methods to perform mentioned task.
    """

    def __init__(self):
        self.head = None

    def add(self, obj):  # add object at the position.
        newnode = Node(obj)

        if self.head is None:
            self.head = newnode
        else:
            tempnode = self.head
            while tempnode.next is not None:
                tempnode = tempnode.next
            tempnode.next = newnode

    def display(self):  # displaying which ever we want to display.
        tempnode = self.head
        while tempnode is not None:
            print(tempnode.object, end=" ")
            tempnode = tempnode.next

    def pop_first(self):  # Removing a node from the beginning.
        tempnode = self.head
        if tempnode is None:
            return -1
        self.head = tempnode.next
        return tempnode.object

    def pop(self):  # Removing a node from the end.
        tempnode = self.head
        previous = self.head
        if tempnode is None:
            return -1
        if tempnode.next is None:
            self.head = None
        while tempnode.next is not None:
            previous = tempnode
            tempnode = tempnode.next
        previous.next = None
        return tempnode.object

    def remove(self, obj):  # Removing a node from the middle.
        tempnode = self.head
        previous = self.head
        if tempnode.object == obj:

            self.head = tempnode.next
        else:
            while tempnode.object != obj:
                previous = tempnode
                tempnode = tempnode.next
            previous.next = tempnode.next

    def size(self):  # Getting size on list.
        tempnode = self.head
        count = 0
        while tempnode is not None:
            count += 1
            tempnode = tempnode.next
        return count

    def search(self, obj):  # It returns a match object.
        tempnode = self.head
        while tempnode is not None:
            if tempnode.object == obj:
                return True
            tempnode = tempnode.next
            return False
        else:
            print("word is not found in a list")
            return False

    def sort(self, obj):  # It can be used to sort the list in both ascending and descending order.
        newnode = Node(obj)
        if self.head is None:
            self.head = newnode
        else:
            tempnode = self.head
            if tempnode.object > obj:
                newnode.next = tempnode
                self.head = newnode
            else:
                previous = self.head
                while tempnode is not None:
                    if tempnode.object > obj:
                        newnode.next = previous.next
                        previous.next = newnode
                        return
                    previous = tempnode
                    tempnode = tempnode.next
                previous.next = newnode

    def get_last(self):  # returns the value of the top.
        tempnode = self.head
        if tempnode is None:
            return -1
        while tempnode.next is not None:
            tempnode = tempnode.next
        return tempnode.object

    def is_empty(self):  # To check the list is empty.
        if self.size() is 0:
            return True
        else:
            return False

    def insert(self, obj):  # added in the first.
        newnode = Node
        newnode.object = obj
        newnode.next = self.head
        self.head = newnode

    def get_head(self):  # it gives a head.
        return self.head

    def get_by_index(self, index):
        tempnode = self.head
        for i in range(index):
            tempnode = tempnode.next
        return tempnode.object

    def delete_by_index(self, index):  # it delete at the index position.
        temp = self.head
        pre = temp
        if index == 0:
            self.head = temp.next
        while index > 0:
            pre = temp
            temp = temp.next
            index -= 1
        pre.next = temp.next

##############################################################################################


class Stack:
    """
    A stack is a collection of objects that supports fast last-in,
    first-out (LIFO) semantics for inserts and deletes.
    """

    def __init__(self):
        self.stack = LinkedList()

    def push(self, obj):  # push data in stack at the end.
        self.stack.add(obj)

    def pop(self):  # pop data from end.
        return self.stack.pop()

    def peek(self):  # returns the value of the top.
        return self.stack.get_last()

    def size(self):  # it gives size of stack.
        return self.stack.size()

    def isEmpty(self):
        return self.stack.is_empty()

#####################################################################################################


class BalancedParentheses:
    def __init__(self):
        """
        Creating object of stack class
        """
        self.stack = Stack()

    def balanced_parentheses(self, string):
        """
        :param string : take one input.
        :return : return true if string is balanced else false
        """

        for i in string:
            if i == '(' or i == '{' or i == '[':  # pushing all open parenthesis in stack.
                self.stack.push(i)
            elif i == ')' or i == '}' or i == ']' and self.stack.peek() is "(":  # peek gives top most parenthesis.

                if self.stack.isEmpty():
                    return False
                else:
                    self.stack.pop()  # it pop the last element in stack.
        if self.stack.size() == 0:
            return True
        else:
            return False

########################################################################################################


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, obj):  # to add object in a queue.
        self.queue.add(obj)

    def dequeue(self):  # delete the last object in a queue.
        return self.queue.pop_first()

    def size(self):  # getting size of queue.
        return self.queue.size()

    def isEmpty(self):
        return self.queue.is_empty()

###############################################################################################

    # Simulate Banking Cash Counter


class CashCounter:
    def __init__(self):
        pass

    @staticmethod
    def cash_counter():
        """
        This is the Program which creates Banking Cash Counter where people come in
        to deposit Cash and withdraw Cash. Have an input panel to add people to Queue
        to either deposit or withdraw money and dequeue the people. Maintain the Cash Balance.

        :return:
        """
        cash = 1000
        deposit = 0
        withdraw = 0
        while True:
            print(" 1 Deposit cash")
            print(" 2 withdraw cash")
            print(" 3 exit")
            choice = int(input("Enter your choice : "))  # here enter your choice to run programs.
            if choice == 1:
                amount = int(input("Enter amount to be deposited: "))  # gives input to deposit.
                if amount == 0:
                    print("Please enter amount again!!")  # condition if input is zero.
                else:
                    deposit += amount  # adding amount in the bank.
                    cash += amount  # while deposit cash will increase.
                    print("Your bank balance is", cash)
            if choice == 2:
                amount = int(input("Enter amount to be withdraw:"))  # gives input to withdraw.
                if amount == 0:
                    print("Please enter amount again!!")  # condition if input is zero.
                else:
                    withdraw -= amount  # subtracting amount from bank.
                    cash -= amount  # while withdraw cash will decrease.
                    print("Your remaining bank balance is", cash)
            if choice == 3:
                print("Have a good day!!")  # while we entered choice 3 exit operation will perform.
            elif choice > 3:
                print("You have only up to 3 in options!!")

###########################################################################################################


class DeQueue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue_from_rear(self, obj):  # Adding in the last
        self.queue.add(obj)

    def enqueue_from_front(self, obj):  # Adding at the first
        self.queue.insert(obj)

    def dequeue_from_rear(self):  # Remove from last
        return self.queue.pop()

    def dequeue_from_front(self):  # Remove from first
        return self.queue.pop_first()

    def size(self):  # it gives size.
        return self.queue.size()

    def is_empty(self):
        return self.queue.is_empty()

######################################################################################################


class PalindromeChecker:
    def __init__(self):
        """
        Creating object of Dequeue for maintain and storing data
        """
        self.dequeue = DeQueue()

    def palindromeChecker(self, string):
        """
        :param string : take input string as parameter for checking string is palindrome or not.
        :return: return boolean value, If string is palindrome then return true else return false.
        """
        for i in range(len(string)):
            self.dequeue.enqueue_from_rear(string[i])
        while self.dequeue.size() > 1:
            if self.dequeue.dequeue_from_front() != self.dequeue.dequeue_from_rear():
                return False
        return True

##################################################################################################

    # Prime Anagrams in the Reverse Order.


class Reverse_Anagram:
    def __init__(self):
        """
        Creating object of stack class
        """
        self.stack = Stack()

    def reverse_prime_anagram(self, a):
        """
        Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack
        using the Linked List and Print the Anagrams in the Reverse Order.
        Note no Collection Library can be used.
        :return:
        """
        from data_structure_programs.anagram_of_prime import primes
        stack_anagram = []
        a = primes(1000)
        self.stack.push(a)
        stack_anagram.append(a)
        return a

#############################################################################################################

    # Print Anagrams from Queue.


class Anagram_Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.queue = Queue()

    def anagrams_queue(self):
        """
        Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Queue
        using the Linked List and Print the Anagrams from the Queue.
        :return:
        """
        from data_structure_programs import prime_anagram
        anagrams_queue = []
        while prime_anagram is 1000:
            self.queue.enqueue(anagrams_queue)
            print()

#############################################################################################################


class BinarySearchTree:
    """
    Number of Binary search trees.
    This class contains methods which can perform the below mentioned methods.
    """
    def __init__(self):
        pass

    def factorial(self, n):
        """
        This method calculates the factorial of a number.
        :param n: The integer input.
        :return: factorial: the calculated factorial of the number n.
        """
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    def catalan_formula(self, nodes):  # Catalan numbers are a sequence of positive integers,
        # where the nth term in the sequence, denoted Cn, is found in the following
        # formula: Cn = (2n)! / ((n + 1)!
        """
        This method uses the catalan formula to find out the number of binary search trees.
        :param nodes:Number of nodes of the binary search tree.
        :return: the number of binary search trees that can be created using these many nodes.
        """
        binary_search_tree_numbers = int(self.factorial(nodes*2)/(self.factorial(nodes+1) * self.factorial(nodes)))
        return binary_search_tree_numbers

    def binary_search_tree(self):
        """
        This method takes in a number of test cases and prints of the number of
        binary search trees for the respective number of nodes.
        """
        test_cases = int(input("Enter a number of test cases: "))
        for i in range(test_cases):
            nodes_input = int(input("Enter the number of nodes: "))
            print("Binary search tree:", self.catalan_formula(nodes_input))





