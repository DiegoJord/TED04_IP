'''promoção, acima de 12 maçãs = 1,00R$ por unidade, menos de uma dúzia = 1,30R$ por unidade'''

n_macas = int(input("Qual o número de maçãs que irá comprar? "))
valor1 = n_macas * 1.00
valor2 = n_macas * 1.30

if n_macas >=12:
    print(f"valor a pagar: R${valor1}")

else:
    print(f"valor a pagar: R${valor2}")