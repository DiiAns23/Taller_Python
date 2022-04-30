from Analizador import Analizador as A

analizador = A()
analizador.Leer('carro')
analizador.Analizar()
carros = analizador.getData()

for carro in carros:
    print(carro.getModelo(), carro.getMarca())
