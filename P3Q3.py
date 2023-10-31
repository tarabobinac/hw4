import string


def theta_j():
    fileNames = ["j0", "j1", "j2", "j3", "j4", "j5", "j6", "j7", "j8", "j9"]
    japanese = dict()
    for letter in string.ascii_lowercase:
        japanese[letter] = 0
    japanese[" "] = 0

    for fileName in fileNames:
        file = open("./languageID/" + fileName + ".txt", "r")
        while True:
            char = file.read(1)
            if not char:
                break

            if char in japanese:
                japanese[char] = japanese[char] + 1

    sum = 0
    for key in japanese:
        sum += japanese[key]

    for key in japanese:
        print(key + ": " + str((japanese[key] + 0.5) / (sum + (27 / 2))))


def theta_s():
    fileNames = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"]
    spanish = dict()
    for letter in string.ascii_lowercase:
        spanish[letter] = 0
    spanish[" "] = 0

    for fileName in fileNames:
        file = open("./languageID/" + fileName + ".txt", "r")
        while True:
            char = file.read(1)
            if not char:
                break

            if char in spanish:
                spanish[char] = spanish[char] + 1

    sum = 0
    for key in spanish:
        sum += spanish[key]

    for key in spanish:
        print(key + ": " + str((spanish[key] + 0.5) / (sum + (27 / 2))))


def main():
    theta_j()
    theta_s()


if __name__ == "__main__":
    main()
