import string
import math

def main():
    #x
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

    #theta_e, theta_j, theta_s
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

    product_e, product_j, product_s = 0, 0, 0
    for key in english:
        product_e += math.log(english[key]) * test[key]
        product_j += math.log(japanese[key]) * test[key]
        product_s += math.log(spanish[key]) * test[key]

    print("e: " + str(product_e))
    print("j: " + str(product_j))
    print("s: " + str(product_s))


if __name__ == "__main__":
    main()