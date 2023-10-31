import string


def main():
    fileNames = ["e0", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9"]
    english = dict()
    for letter in string.ascii_lowercase:
        english[letter] = 0
    english[" "] = 0

    for fileName in fileNames:
        file = open("./languageID/" + fileName + ".txt", "r")
        while True:
            char = file.read(1)
            if not char:
                break

            if char in english:
                english[char] = english[char] + 1

    sum = 0
    for key in english:
        sum += english[key]

    for key in english:
        print(key + ": " + str((english[key] + 0.5) / (sum + (27 / 2))))


if __name__ == "__main__":
    main()
