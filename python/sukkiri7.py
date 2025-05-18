import math
import http.client

text = input('何を記録しますか >>')
file = open('diary.txt', 'a')
file.write(text + '\n')
file.close()

print(f'円周率は{math.pi}です')
print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です')
print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です')

conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
text = response.read()
print(text)
conn.close()