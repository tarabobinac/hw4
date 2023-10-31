import string
import numpy as np
import math

e = j = s = 1 / 3
s10, s11, s12, s13, s14, s15, s16, s17, s18, s19 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
e_test_docs = [s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]

for doc in e_test_docs:
    for letter in string.ascii_lowercase:
        doc[letter] = 0
    doc[" "] = 0

for i in range(10, 20):
    file = open("./languageID/s" + str(i) + ".txt", "r")
    while True:
        char = file.read(1)
        if not char:
            break

        if char in e_test_docs[i - 10]:
            e_test_docs[i - 10][char] = e_test_docs[i - 10][char] + 1

fileNames_e = ["e0", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9"]
fileNames_j = ["j0", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9"]
fileNames_s = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]

english, japanese, spanish = dict(), dict(), dict()

for letter in string.ascii_lowercase:
    english[letter], japanese[letter], spanish[letter] = 0, 0, 0

english[" "], japanese[" "], spanish[" "] = 0, 0, 0

for i in range(10):
    file_e = open("./languageID/" + fileNames_e[i] + ".txt", "r")
    file_j = open("./languageID/" + fileNames_j[i] + ".txt", "r")
    file_s = open("./languageID/" + fileNames_s[i] + ".txt", "r")

    while True:
        char = file_e.read(1)
        if not char:
            break

        if char in english:
            english[char] = english[char] + 1

    while True:
        char = file_j.read(1)
        if not char:
            break

        if char in english:
            japanese[char] = japanese[char] + 1

    while True:
        char = file_s.read(1)
        if not char:
            break

        if char in english:
            spanish[char] = spanish[char] + 1

sum_e, sum_j, sum_s = 0, 0, 0
for key in english:
    sum_e += english[key]
    sum_j += japanese[key]
    sum_s += spanish[key]

for key in english:
    english[key] = (english[key] + 0.5) / (sum_e + (27 / 2))
    japanese[key] = (japanese[key] + 0.5) / (sum_j + (27 /2))
    spanish[key] = (spanish[key] + 0.5) / (sum_s + (27 / 2))

for i in range(10):
    product_e, product_j, product_s = 0, 0, 0
    for key in english:
        product_e += math.log(english[key]) * e_test_docs[i][key]
        product_j += math.log(japanese[key]) * e_test_docs[i][key]
        product_s += math.log(spanish[key]) * e_test_docs[i][key]

    denominator_e = product_e - math.log(3)
    denominator_j = product_j - math.log(3)
    denominator_s = product_s - math.log(3)
    ePlusJPlusS = np.logaddexp(np.logaddexp(denominator_e, denominator_j), denominator_s)

    pred_e = denominator_e - ePlusJPlusS
    pred_j = denominator_j - ePlusJPlusS
    pred_s = denominator_s - ePlusJPlusS

    if pred_e > pred_j and pred_e > pred_s:
        print(str(i + 1) + ". e")
    elif pred_j > pred_e and pred_j > pred_s:
        print(str(i + 1) + ". j")
    elif pred_s > pred_e and pred_s > pred_j:
        print(str(i + 1) + ". s")
