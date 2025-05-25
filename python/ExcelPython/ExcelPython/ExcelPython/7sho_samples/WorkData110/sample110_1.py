import openpyxl
import xml.etree.ElementTree as ET
wb = openpyxl.load_workbook('新店長.xlsx')
ws = wb.active
sdata = []
for row in ws.iter_rows(min_row=2):
    sdata.append([row[0].value, row[1].value])
tree = ET.parse('shoplist02.xml')
for tnum in range(len(sdata)):
    tshop = tree.find("shop[name='" +
                      sdata[tnum][0] + "']")
    tshop.find('manager').text = sdata[tnum][1]
tree.write('shoplist03.xml', encoding='utf-8',
           xml_declaration=True)
