from xlrd import open_workbook
from random import shuffle

def main(file_loc):
    r_words = []

    wb = open_workbook(file_loc)
    sheet = wb.sheets()[0]

    number_of_rows = sheet.nrows
    indexes = [i for i in range(number_of_rows)]
    if input("randome? (\"y\" for yes) ") == "y":
        shuffle(indexes)

    count = 0
    isExit = False
    for i in indexes:
        count += 1
        is_to_next = False
        word  = sheet.cell(i,0).value
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
            elif res == "r":
                is_to_next = False
                print(number_of_rows - count)
            elif res == "exit":
                isExit = True
                break
            elif res != "" and res != "y":
                r_words.append(word)
                is_to_next = True
                print("Added to review list")
        
        if isExit == True:
            break
        print("----------------------------")

    with open('review_list.txt', 'w') as f:
        for item in r_words:
            f.write("%s\n" % item)


if __name__=="__main__":
    main("./harsh.xlsx")