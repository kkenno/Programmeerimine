print "\033[y;xH" - viib kursori koordinaatidele x ja y
print "\033[2J"


import sys

def kursor(x, y, t):
    sys.stdout.write("\033[" + str(y) + ";" + str(x) + "H" + t)

kursor(50, 30, "tekst")
