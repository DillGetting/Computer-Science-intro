import stdio
import sys
import math
'''number_list = []
def average(number_list):
    sum = 0
    for num in number_list:
        sum += num
    return sum / len(number_list)'''

r = 2
def aoc(r):
    area = math.pi * r**2
    return area
print("r is: {}".format(r))
print("area is: {}".format(aoc(r)))
print("r is: {}".format(r))

def testMyCode():
    assert(add(1,1)==2)
    assert(add(1, 1.0) ==2.0)
    assert(add(1.0,1.0) == 2)

def main():
    arg1 = sys.argv[1]
    if arg1 == '-t':
        testMyCode()
    else:
        print("1 and 1 is: ")
if __name__ == '__main__':
    testMyCode()
