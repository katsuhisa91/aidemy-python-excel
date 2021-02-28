import openpyxl

wb = openpyxl.Workbook()
wb.create_sheet()
wb.save('sample.xlsx')
