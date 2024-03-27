"""## Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas."""

distancia = int(input("Digite a distância em Km: "))

valor_passagem = 0.50 if distancia <= 200 else 0.35

resultado = distancia * valor_passagem

print(f"O valor da passagem é R${resultado:.2f}")

"""## Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%."""

salario = float(input("Digite o salário do funcionário: "))

aumento = 0.10 if salario > 1250 else 0.15

resultado_aumento = salario * aumento

print(f"O aumento será de R${resultado_aumento:.2f}")