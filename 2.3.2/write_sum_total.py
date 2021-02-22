import openpyxl

wb = openpyxl.load_workbook('買い物メモ.xlsx')
sheet = wb['Sheet1']
# セルC2からセルC4までの合計値を求める数式を、セルC5に入力してください
sheet.cell(row=5, column=3).value = '=C2+C3+C4'
wb.save('買い物結果.xlsx')