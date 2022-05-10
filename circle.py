import stddraw
import random
import math
import sys

n = int(sys.argv[1])

p = float(sys.argv[2])

stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)
stddraw.setPenRadius(.01)
stddraw.setPenColor(stddraw.GRAY)

x0 = 0.0
y0 = 0.0

t = 0.0
while t <= 360.0:
    theta = math.radians(t)
    r = math.sin(n * theta)
    x1 = r * math.cos(theta)
    y1 = r * math.sin(theta)
    stddraw.line(x0, y0, x1, y1)
    x0 = x1
    y0 = y1
    t += 0.1
stddraw.show()


#stddraw.circle(0,0,1)
#stddraw.show()
'''an angle is the input there are 360 degress in an angle
have a circle of r 1 centered at 0,0 
right trianle with any angle has hypot of 1
need to get x and y
sin opp of hyp gives y over 1
cos is opp of adj gives x over 1
increment it by the angle
add to the angle
a = a gives another point
have a set of points p1 p2... pn
store the pints in an array or list,
pxy = [p1, p2...]
each point is an x and y value
probability is between 0 and 1
if p == .166
if you get a one you draw a line 
if any other value you do not draw a line
then move to p2 if you get a one draw line
.116 is the probability of rolling a 1 on a die
'''