from openpyxl import Workbook

wb = Workbook()
name = './Modulo 2/Semana 1/Dia3/test.xlsx'
ws1 = wb.active
ws1.title = 'Planilha1'

#Adicionando os dados

data = [
    ['Ano', 'Lucros', 'Despesas'],
    [2019, '25%', '10%'],
    [2020, '30%', '15%'],
    [2021, '35%', '20%'],
    [2022, '40%', '25%'],
    [2023, '45%', '30%'],
    [2024, '50%', '35%'],
]

ws2 = wb.create_sheet(title='Pi')
ws2['D2'] = 3.14

for line in data:
    ws1.append(line)

wb.save(filename=name)