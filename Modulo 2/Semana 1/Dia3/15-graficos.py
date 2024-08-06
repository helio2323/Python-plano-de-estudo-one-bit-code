from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, series

wb = Workbook()
ws = wb.active

data = [
    ['Ano', 'Lucros', 'Despesas'],
    [2019, 40, 30],
    [2020, 50, 40],
    [2021, 60, 50],
    [2022, 70, 60],
    [2023, 80, 70],
    [2024, 90, 80], 
]

for d in data:
    ws.append(d)
    
#criacao do grafico

chart = AreaChart()
chart.title = "Lucros e Despesas"
chart.style = 12
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcentagem"

categorias = Reference(
    ws,
    min_col=1,
    min_row=1,
    max_row=7
)

dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=7
)

chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)
ws.add_chart(chart, "A10")

    
wb.save('./Modulo 2/Semana 1/Dia3/graficos.xlsx')