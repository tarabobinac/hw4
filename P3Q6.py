import string
import numpy as np
import math

xGivenE = -7841.865447060635
xGivenJ = -8771.433079075032
xGivenS = -8467.282044010557
e = j = s = 1/3

test = dict()
for letter in string.ascii_lowercase:
    test[letter] = 0
test[" "] = 0

e10 = open("./languageID/e10.txt", "r")
while True:
    char = e10.read(1)
    if not char:
        break
    if char in test:
        test[char] = test[char] + 1

denominator_e = xGivenE - math.log(3)
denominator_j = xGivenJ - math.log(3)
denominator_s = xGivenS - math.log(3)
ePlusJPlusS = np.logaddexp(np.logaddexp(denominator_e, denominator_j), denominator_s)

print(ePlusJPlusS)
print(denominator_e - ePlusJPlusS)
print(denominator_j - ePlusJPlusS)
print(denominator_s - ePlusJPlusS)