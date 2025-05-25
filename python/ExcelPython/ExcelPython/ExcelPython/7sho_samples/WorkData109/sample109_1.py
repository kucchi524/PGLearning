import xml.etree.ElementTree as ET
import openpyxl
tree = ET.parse('shoplist01.xml')
root = tree.getroot()
wb = openpyxl.Workbook()
ws = wb.active
titlerow = [i.tag for i in root[0]]
ws.append(titlerow)
for elems in root:
    datarow = [i.text for i in elems]
    ws.append(datarow)
wb.save('店舗情報01.xlsx')
