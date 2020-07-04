from xlrd import open_workbook

def main(file_loc):
    r_words = []

    wb = open_workbook(file_loc)
    sheet = wb.sheets()[1]
    number_of_rows = sheet.nrows
    for i in range(number_of_rows):
        word  = sheet.cell(i,0).value
        if word =="":
            continue
        print(word)
        print("Know this one?")
        res = input(">>> ")
        if res == "c":
            print(number_of_rows - i)
            res = input(">>> ")
        if res == "num":
            print(len(r_words))
            res = input(">>> ") 
        if res != "" and res != "y":
            r_words.append(word)
            print("Added to review list")
        print("----------------------------")

    with open('review_list.txt', 'w') as f:
        for item in r_words:
            f.write("%s\n" % item)


if __name__=="__main__":
    main("./Vocab_grabbed_on_the_way.xlsx")