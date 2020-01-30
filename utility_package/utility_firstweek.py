"""This is a utility_firstweek file which contains Utility class having different methods.
   Author: Rutuja Tikhile
   Date: 13/01/2020
"""
import math
import random


class Utility:
    """ This is a Utility class which contains logic performing the mentioned task.
    """

    @staticmethod
    def string_replace(string):
        """Method to replace string.

        This method will take a string and replace it with a given user name.

        :param string:This is the input from the user by which given string has to be replaced.
        :return:Print the String with User Name.
        """

        name = "Hello <<UserName>>, How are you?"
        if len(string) > 3 and string.isalnum() and (string.isnumeric() == False):  # string should be greater than 3,
            # string may be alphanumeric and make condition false if string is numeric.
            new_string = name.replace("<<UserName>>", string).title()  # .replace is used to replace the "<<UserName>>"
            # with user entered string and .title() used to convert the first character in each word to
            # Uppercase and remaining characters to Lowercase.
            return new_string  # this will return new replaced string.
        else:
            print("User name should be greater than 3!!")
            print("User name should contain alphanumeric values not numbers!!")

    @staticmethod
    def toss_coin(trails):
        """
        Method to flip coin randomly.
        This method will randomly select heads and tails based on random value generated.
        :param trails:The number of trails to Flip Coin.
        :return:This will return heads or tails.
        """

        heads = 0
        tails = 0
        for i in range(trails):
            toss = random.uniform(0, 1)  # import random function for generating random values.
            # .uniform gives you floating values.
            if toss > 0.5:
                print("tails")
                tails += 1

            else:
                print("heads")
                heads += 1
        print("Number of heads coming: ", heads)
        print("Number of tails coming: ", tails)
        hp = heads / trails * 100
        tp = tails / trails * 100
        print("percentage of head= ", hp)
        print("percentage of tail= ", tp)

    @staticmethod
    def leap_year(year):
        """This method tells the entered year is leap or not.
        :param year: enter year to check year is leap or not.
        :return:Year is leap or not.
        """
        if (year > 1000) and (year < 9999):  # year should be in range between 1000 to 9999.
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # condition to check leap year.
                return "Leap year"
            else:
                return "Not a Leap year"
        else:
            return "Ensure it is a 4 digit number."

    @staticmethod
    def power_of2(expo):
        """
        This method gives us the power of 2.
        :param expo:This is the input from the user for exponent.
        :return: This will return the user entered number by power of 2.
        """
        if expo > 31:
            print("Number should be less than 31")

        else:
            arr = []  # creating array for all the values in the power.
            for i in range(1, expo + 1):
                power = 2 ** i  # formula for getting power of the number.
                print("prints a table of the powers of 2: ", power)
                arr.append(power)  # .append adds its argument as a single element to the end of a list.
            return arr

    @staticmethod
    def nth_harmonic(n):
        """
        This is the method to find nth harmonic number.
        :param n: type of int in which n(number) given by the user to find the nth harmonic value of that number.
        :return: nth harmonic number of the entered value.
        """

        harmonic = 1
        for i in range(2, n + 1):  # defining range for n from 2 to n+1.
            harmonic += 1 / i  # formula to find nth harmonic number.
        print("Nth harmonic number: ", harmonic)
        return harmonic

    @staticmethod
    def prime_fac(n):
        """
        This is the method which gives us prime factors of user entered number.
        :param n:Number from the user to find the factors of that number.
        :return:Prime factors of entered number.
        """
        arr = []
        for i in range(2, n):  # defining range from 2 to user entered number n.
            while n % i == 0:
                print("Prime Factors of entered number: ", i)
                n = n / i
                arr.append(i)

        if n > 1:
            print("Factors of entered number: ", n)
            arr.append(n)
        return arr

    @staticmethod
    def two_d_array(m, n):
        """
        This is the method to create 2 dimensional array in memory to read in m rows and n cols.
        :param m:m is the number of rows.
        :param n:n is number of cols.
        return:Two D-array.
        """
        matrix = []
        print("Enter the entries row wise:")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            matrix.append(a)
        for i in range(m):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

    @staticmethod
    def sum_of_int(arr, n):
        """
        This is the method which find distinct triples (i, j, k) such that a[i] + a[j] + a[k]
        is equals to user entered number.

        :param arr:Take an array.
        :param n:length of an array.
        :return:distinct triples from array.
        """

        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        print("Triples: ", arr[i], arr[j], arr[k])

    @staticmethod
    def distance(x, y):
        """
        This is the method which calculate distance from the point (x, y)
        to the origin (0, 0) we have to find distance.
        :param x:x parameters are given by the user.
        :param y:y parameters are given by the user.
        :return:calculated distance from the given formula.
        """

        distance = math.sqrt(math.pow((x - 0), 2) + math.pow((y - 0), 2))  # formula for finding distance.
        print("Distance between two points: ", distance)
        return distance

    @staticmethod
    def quadratic(a, b, c):
        """
        This is the method to find the roots of the equation a*x*x + b*x + c.
        :param a:Parameters from the user.
        :param b:Parameters from the user.
        :param c:Parameters from the user.
        :return:The 2 roots of the equation.
        """
        import cmath  # import complex math module, it provides access to mathematical functions for complex numbers.
        # it is used to convert from the native rectangular coordinates to polar coordinates.

        if a == 0:  # If a is 0, then equation is not quadratic, but linear.
            print("Invalid")
            return -1
        delta = b * b - 4 * a * c  # formula to find delta.
        if delta > 0:
            print("Roots are real and different ")
            print((-b + math.sqrt(delta)) / (2 * a))
            print((-b - math.sqrt(delta)) / (2 * a))
        elif delta == 0:
            print("Roots are real and same")
            print(-b / (2 * a))
        else:  # delta < 0
            print("Roots are complex")
            print(- b / (2 * a), " + i", cmath.sqrt(delta))
            print(- b / (2 * a), " - i", cmath.sqrt(delta))

    @staticmethod
    def wind_chill(t, v):
        """
        This is the method which prints the wind chill.
        Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
        the National Weather Service defines the effective temperature (the wind chill)
        to be (result) by using formula.
        :param t: The formula is not valid if t is larger than 50 in absolute value.
        :param v: v should be larger than 120 or less than 3
        :return:wind chill.
        """
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)  # this is the given formula for w
        return round(w, 2)

    @staticmethod
    def gambler(stake, goal, times):
        """
        This is the method in which a gambler who start with $stake and place fair $1 bets
        until he/she goes broke (i.e. has no money) or reach $goal.
        Keeps track of the number of times he/she wins and the number of bets he/she makes.
        :param stake:Enter stake.
        :param goal:Enter goal.
        :param times:Enter number of trails.
        :return:Print Number of Wins and Percentage of Win and Loss.
        """
        bets = 0
        wins = 0
        for i in range(times):
            cash = stake
            while (cash > 0) and (cash < goal):
                bets += 1
                if random.randint(0, 1) == 0:
                    cash += 1
                else:
                    cash -= 1
            if cash == goal:
                wins += 1
        print(str(100 * wins / times) + " % wins")
        print("avg bets:" + str(bets // times))

    @staticmethod
    def stop_watch():
        """
        This is the method which is used for measuring the time that elapses between the start and end clicks.

        :return:Print the elapsed time.
        """
        import datetime

        input("Press any key to start the stopwatch: ")
        start = datetime.datetime.now()
        input("Press any key to end the stopwatch: ")
        end = datetime.datetime.now()

        result = end - start
        return result

    @staticmethod
    def insertion_sort_a(list):
        """
        This method reads in strings and prints them in sorted order using insertion sort.

        :param list:List of array.
        :return: Print the Sorted List.
        """
        for i in range(1, len(list)):
            current_ele = list[i]
            pos = i

            while current_ele < list[pos - 1] and pos > 0:
                list[pos] = list[pos - 1]
                pos = pos - 1
            list[pos] = current_ele
        return list

    @staticmethod
    def bubble_sort_a(nums):
        """
        This method reads in integers prints them in sorted order using Bubble Sort.

        :param nums:number of list in an array.
        :return:Print the Sorted List.
        """
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return nums

    @staticmethod
    def prime_num_in_range():
        """
        This is the method which gives prime number in the range between 0 to 1000.
        :return:List of prime number between 0 to 1000.
        """
        list = []
        for num in range(0, 1000):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        return list
#########################################################################################################

    @staticmethod
    def is_prime(num):
        temp = 0
        for i in range(1, num+1):
            if num % i == 0:
                temp += 1
        if temp == 2:
            return True
        else:
            return False
