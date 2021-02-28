## 出力に、Noneを表示させたくない場合

print()で画面出力する前に、if文をつかい、値があるかどうかを事前に判定させればよい。

```python
for cell in list(sheet.columns)[1]:
    if cell.value:
        print(cell.value)
```

forループとrange()関数をつかった場合も、同様に判定をはさむことで回避できる。
（read_cell.pyでは、range(2, 5)として、そもそも含めいないようにしているが。）

```python
for i in range(1, 5):
    if sheet.cell(row=i, column=2).value:
        print(sheet.cell(row=i, column=2).value)
```
