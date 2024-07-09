from openpyxl import Workbook

print('Lendo dados do arquivo de texto')

file_txt = open('./Modulo 2/Semana 1/Dia3/gastos.txt', 'r', encoding='utf-8')
file = file_txt.read()

list_data = file.splitlines()

for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(',')

wb = Workbook()

ws = wb.active

for row in list_data:
    ws.append(row)

wb.save('./Modulo 2/Semana 1/Dia3/gastos.xlsx')