#Compose a program that reads in a sequence of integers and
#writes both the integer
#that appears in a longest consecutive run and the length of the run.


import stdio
import sys

#reading in the standard input


if stdio.isEmpty():
    stdio.writeln('nothing for this program to find')
    sys.exit()

userin = stdio.readInt();
count = 1
optimal = userin
bestOpt = count


while not stdio.isEmpty():

    now = stdio.readInt()

    if now == userin:
        count += 1
    else:
        userin = now
        count =1

    if count > bestOpt:
        bestOpt = count
        optimal = now
        break

#stdio.writeln('Longest run: ' + str(bestOpt) + \ ' consecutive ' + str(optimal) + 's')
stdio.writeln('Longest run: ' + str(bestOpt) + \
              ' consecutive ' + str(optimal) + 's')
