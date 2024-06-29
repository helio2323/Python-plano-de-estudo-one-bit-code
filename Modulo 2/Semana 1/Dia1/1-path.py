from pathlib import Path

p1 = Path('./Modulo 2/Semana 1/Dia1', 'teste.txt')

print(p1)
print(type(p1))
print(p1.name)
print(p1.stem)
print(p1.suffix)
print(p1.exists())

if p1.exists():
    with open(p1, 'r', encoding='utf-8') as f:
        print(f.read())

p2 = Path('./Modulo 2/Semana 1/Dia1')
print(list(p2.iterdir()))