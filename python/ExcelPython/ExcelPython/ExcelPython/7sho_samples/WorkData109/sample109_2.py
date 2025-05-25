import xml.etree.ElementTree as ET
import openpyxl
tree = ET.parse('shoplist01.xml')
root = tree.getroot()
wb = openpyxl.Workbook()
ws = wb.active
titlerow = ['コード', '店名']
ws.append(titlerow)
for elems in root:
    datarow = [int(elems.get('code')),
               elems.find('name').text]
    ws.append(datarow)
wb.save('店舗情報02.xlsx')
