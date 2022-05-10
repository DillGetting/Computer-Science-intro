import sys
import stdio
import stddraw
import numpy

zip = str(sys.argv[1])
zip = [int(i) for i in str(zip)]
# Zip with zero stripped
HaKeyNum = list(filter(lambda a: a != 0, zip))
HaKey = 0
# this creates the list for y cordinates
ycords = []
# Font properties
stddraw.setFontSize(18)

# this is the starting x value for drawing the bar code
x = 6

# canvas size and scale is set here
stddraw.setCanvasSize(900, 900)
stddraw.setXscale(0, 24)
stddraw.setYscale(0, 8)

# This is a dictionary of all y values for bar codes
bars = {0: [2, 2, 1, 1, 1, ], 1: [1, 1, 1, 2, 2], 2: [1, 1, 2, 1, 2],
        3: [1, 1, 2, 2, 1], 4: [1, 2, 1, 1, 2], 5: [1, 2, 1, 2, 1],
        6: [1, 2, 1, 2, 1], 7: [2, 1, 1, 1, 2], 8: [2, 1, 1, 2, 1],
        9: [2, 1, 2, 1, 1]}

# This places all the y cords in a list
for i in zip:
    ycords.append(bars[i])

# This adds the start and end bar heigts as well as flattens the list
ycords = list(numpy.concatenate(ycords).flat)
ycords.insert(0, 2)
ycords.append(2)

# This draws the bars via listed y cords and incrementing the x value
for i in ycords:
    x = x + .25
    stddraw.line(x, .5, x, i)

for i in HaKeyNum:
    HaKey = HaKey + i

HaKey = HaKey % 10

stddraw.text(4.5, 1, str(sys.argv[1]))
print(zip)
print(ycords)
print(HaKey)
stddraw.show()