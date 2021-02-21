import openpyxl

wb = openpyxl.load_workbook('買い物メモ.xlsx')
sheet = wb['Sheet1']
b3_value = sheet.cell(row=3, column=2).value

print(b3_value)