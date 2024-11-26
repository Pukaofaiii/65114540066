from openpyxl import load_workbook
wb = load_workbook('Me & My partner.xlsx')


g = []

for row in wb.active:
    val = [cell.value for cell in row]
    if val[1] == 'My Github User' and val[2] == "My partner's github user":
        continue
    if val[1] is not None and val[2] is not None:
        pair = tuple(sorted((val[1],val[2])))
        g.append(pair)

unique_pairs = set(g)

print(g)
print(unique_pairs)