from xlrd import open_workbook
from random import shuffle

def main(file_loc):
    r_words = []
    r_definations = []

    input_file = input("x or t: ")
    if input_file =="x":
        wb = open_workbook(file_loc)
        sheet = wb.sheets()[1]
        words = sheet.col_values(0)
        definations = sheet.col_values(1)
    else:
        f1 = open("review_list.txt", "r")
        f2 = open("review_definition.txt", "r", encoding="utf-8")
        words = [x[0:-1] for x in f1.readlines()]
        definations = [x[0:-1] for x in f2.readlines()]
        
    number_of_rows = len(words)
    indexes = [i for i in range(number_of_rows)]

    if input("randome? (\"y\" for yes) ") == "y":
        shuffle(indexes)

    count = 0
    isExit = False
    for i in indexes:
        count += 1
        is_to_next = False
        word = words[i]
        if word =="":
            continue
        print(word)
        print("Know this one?")
        while not is_to_next:
            is_to_next = True
            res = input(">>> ")
            if res == "c":
                is_to_next = False
                print(len(r_words))
            elif res == "f":
                is_to_next = False
                print(definations[i])
            elif res == "r":
                is_to_next = False
                print(number_of_rows - count)
            elif res == "exit":
                isExit = True
                break
            elif res != "" and res != "y":
                r_words.append(word)
                r_definations.append(definations[i].split('\n')[0])
                is_to_next = True
                print("Added to review list")
        
        if isExit == True:
            break
        print("----------------------------")

    with open('review_list.txt', 'w') as f:
        for item in r_words:
            f.write("%s\n" % item)

    with open('review_definition.txt', 'w', encoding="utf-8") as f:
        for item in r_definations:
            f.write("%s\n" % item)


if __name__ == "__main__":
    main("./harsh.xlsx")