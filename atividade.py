# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
numerouser = int(input("digite seu numero"))
for i in range(1, 11):
    resultado = numerouser * i 
    print(f"{numerouser} * {i}  = {resultado}")