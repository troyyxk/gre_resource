from random import shuffle
import PyPDF2
from tika import parser
import xlsxwriter

file = open("./gre_core_word.txt", "r", encoding="utf8")

lines = file.readlines()

no_space_lines = []
for line in lines:
    line = line[:-1]
    if " " not in line and line != "" and len(line)<25 and (line.isupper() or line.islower()):
        no_space_lines.append(line)

definitions = []

for line in no_space_lines:
    definitions.append(lines[(lines.index(line+'\n') + 2)])

workbook = xlsxwriter.Workbook('tmp.xlsx')
worksheet = workbook.add_worksheet()

for i in range(len(no_space_lines)):
    worksheet.write(i, 0, no_space_lines[i])
    worksheet.write(i, 1, definitions[i])

workbook.close()

print(no_space_lines)
print(definitions)
