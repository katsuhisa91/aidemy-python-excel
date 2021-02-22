import openpyxl

wb = openpyxl.load_workbook('sample.xlsx')
sheet = wb['Sheet1']
sheet.cell(row=2, column=2).value = 'hello world'
wb.save('sample.xlsx')