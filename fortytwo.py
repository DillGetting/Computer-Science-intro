
import stdio
import stddraw
import sys

stddraw.setCanvasSize(900, 900)
stddraw.setXscale(-100, 100)
stddraw.setYscale(-100, 100)

stddraw.circle(.5, 5.0, 6.0)
stddraw.circle(.5, 19.0, 20.0)

stddraw.line(8.0, 11.0, 10.0, 18.0)
stddraw.line(10.0, 18.0, 11.0, 11.0)
stddraw.line(11.0, 11.0, 8.0, 11.0)

stddraw.line(10.0, 18.0, 8.0, 11.0)
stddraw.line(8.0, 11.0, 4.0, 11.0)
stddraw.line(4.0, 11.0, 10.0, 18.0)

#it is backwards and crooked but i see a face there.
stddraw.show()