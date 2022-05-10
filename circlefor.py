import random
import stddraw

stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)
stddraw.setPenRadius(.01)
for i in range(1000):
    x = -1.0 + 2.0*random.random()
    y = -1.0 + 2.0*random.random()
    if x*x + y*y <= 1.0:
        stddraw.point(x,y)
stddraw.show()


#will draw all points that are in the cirlce in the range of 1000 or whatever
