def countWords():
    fileName = input(" Enter File Name ")
    file = open(fileName, 'r')
    words = 0

    for i in file:
        w = i.split()
        words = words + len(w)

    print(words)

countWords()