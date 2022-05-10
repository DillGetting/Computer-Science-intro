import sys
import stdio
import stdarray
import stddraw
import instream
import outstream

infile = instream.InStream(sys.argv[1])
out = outstream.OutStream('OUTBITCH.txt')

list = []

while infile.hasNextLine():
    list.append(infile.readLine())

for l in list:
    out.writeln(l)



