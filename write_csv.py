f1 = open("review_list.txt", "r")
f2 = open("review_definition.txt", "r", encoding="utf-8")
words = [x[0:-1] for x in f1.readlines()]
definations = [x[0:-1] for x in f2.readlines()]

with open('tmp.txt', 'w', encoding="utf-8") as f:
    for i in range(len(words)):
        f.write(words[i])
        f.write('%')
        f.write(definations[i])
        f.write('\n')
