def primes(n):
    array = [i for i in range(2,n+1)]
    p = 2

    while p <= n:
        i = 2*p
        while i <= n:
            array[i-2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]


def anagram(a):
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i)) == sorted(str(j))):
                anagram_list.append(i)
    return anagram_list
