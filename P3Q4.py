import string


def main():
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

    for character in test:
        print(character + ": " + str(test[character]))


if __name__ == "__main__":
    main()
