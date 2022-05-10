"""

"""
import math

def finded(myl, search):
    for value in myl:
        if value == search:
            return value
    return None


myl = ['ted', 'dil', 'bomba']

myv = find(myl, 'ted')
print(myv)


def finds(myl, search):
    for index, value in enumerate(myl): # n
        if value == search: # 1
            return index #1/n
    return None # 1/n

"""
need more information to attache to the list liek ordering
    after ordering you have reasoning to limun the search
        
        take the list
            find the middle
                    then test for the value
                        if 5 < 9 for example you know what side of the list
                Then keep finding the midpoints in each partition of your list
                That is log(2)n search
                low = 0
                
"""

def find(search, term):
    insert_sort(search) # this is one of the keys and runs different then logn
    left = 0 # all depends
    right = len(search)
    while right - left > 0: # the rest is log n binary searching
        middle = left + math.floor((right - left) / 2)
        if search is term[middle]:
            return middle
        if search < term[middle]:
            right = middle
        else:
            left = middle + 1
    return None

    # def elapsedTime(self):
    #     return time.time() - self._creationTime


def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]


def insert_sort(a): # this is exponential n^2 nested loops
    n = len(a) # only uses a in memmory
    for i in range(1, n):
        j = i
        while (j > 0) and (a[j] < a[j-1]):
            exchange(a, j-1, j)
            j -= 1

# insert fort is similar to bubble but kinda the reverse
# insert sort is considered a little slower than bubble but still n^2
# normally bubble is better and both are not great solutions


def bubble(sort): # each element swaps positions instaed of binary
    for i in range(len(sort)): # this then eventually orders a list through this
        for j in range(i, len(sort)): # is bubbles up to the top for numbers
            if sort[j] < sort[i]:
                temp = sort[i] # this is the extra memory space, extra variable
                sort[i] = sort[j]
                sort[j] = temp

# process left side then right
# gives n(log(n) and 2 steps vertically
# much quicker then other sorts
# partitioning phase and then base case
# probably recursive
#  // 2 is integer division
# can sort anything as long as there is a comparater


def merge():


#  stable sort will put the elemnts from the comparater in order
# unstable will maybe be out of order
