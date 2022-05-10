import sys
import stdio
import stddraw
import numpy

zip = int(sys.argv[1])
zip = [int(i) for i in str(zip)]
#Zip with zero stripped
HaKey = list(filter(lambda a: a != 0, zip))



print(HaKey)


# zipcode = int(sys.argv[1])

totalzip = 0
zipcode = 0
while not stdio.isEmpty():
    zipcode = stdio.readInt()
    stdio.readInt()
stdio.write(zipcode)



