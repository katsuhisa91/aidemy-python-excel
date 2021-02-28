import openpyxl

wb = openpyxl.load_workbook('sample.xlsx')
sheet = wb['Sheet1']

for cell in list(sheet.columns)[1]:
    print(cell.value)

# こちらでも可
# for i in range(1, 5):
#     print(sheet.cell(row=i, column=2).value)
