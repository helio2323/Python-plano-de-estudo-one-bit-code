"""
## Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1. Cada produto deve ter um preço e um nome.
2. A classe deve ter um método construtor e o método dundle str.
3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto."""

class Produto:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"Produto: {self.nome}"
    
    def desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)
        return self.preco

celular = Produto("Celular", 1000)
print(celular)
print(celular.desconto(10))