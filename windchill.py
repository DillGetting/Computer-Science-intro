# windchill.py
# ---------------------------------------------

# Compose a program that takes two floats t and v from the command line
# and writes the wind chill.

import sys
import stdio

# Taking user inputs from the command line.
temp = float(sys.argv[1])
windSpeed = float(sys.argv[2])

# Computing the wind chill based on user input.
chill = 35.74 + (0.6215 * temp) + (0.4275 * temp - 35.75) * (windSpeed ** 0.16)

# Printing the temperature, wind speed, and wind chill.
stdio.writeln('Temperature = ' + str(temp))
stdio.writeln('Wind speed = ' + str(windSpeed))
stdio.writeln('Wind chill = ' + str(chill))