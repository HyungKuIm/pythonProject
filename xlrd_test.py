import xlrd
import pprint

wb = xlrd.open_workbook('data/src/sample.xls')

print(type(wb))

print(wb.sheet_names())

sheets = wb.sheets()

print(type(sheets))

print(type(sheets[0]))

sheet = wb.sheet_by_name('sheet1')

print(type(sheet))

cell = sheet.cell(1, 2)

print(cell)

print(type(cell))

print(cell.value)

print(sheet.cell_value(1, 2))

col = sheet.col(1)

print(col)

print(type(col[0]))

col_values = sheet.col_values(1)

print(col_values)

print(sheet.row_values(1))

pprint.pprint([sheet.row_values(x) for x in range(4)])