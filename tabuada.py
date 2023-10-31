# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

print("saiba a tabuada de qualquer numero")
numero = int(input("insira o numero:"))
for mult in range(0, 11):
   resultado = (numero * mult)
   print(f"{numero} x {mult} = {resultado}")
