import openpyxl

wb = openpyxl.load_workbook('見積書.xlsx')
sheet = wb['見積書']
sheet['N30'].value = '=sum(N18:N29)'
sheet['N32'].value = '=N30*1.1'

wb.save('見積書_完成版.xlsx')