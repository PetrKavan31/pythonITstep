
with open('newTest.txt') as fr:
    data = fr.read()
    print(data)
    lines = data.split()
    nWords = 0
    for words in lines:
        if not words.isnumeric():
            nWords += 1
