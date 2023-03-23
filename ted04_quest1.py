'''1. Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere
o valor zero como positivo)'''

numero = int(input("digite um número: "))

if numero >= 0:
    print(f"o número {numero} é positivo")

else:
    print(f"o número {numero} é negativo")