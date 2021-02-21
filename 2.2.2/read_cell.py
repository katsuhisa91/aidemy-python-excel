import openpyxl

wb = openpyxl.load_workbook('sample.xlsx')
sheet = wb['Sheet1']
b2_value = sheet.cell(row=2, column=2).value

print(b2_value)