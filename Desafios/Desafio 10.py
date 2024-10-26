#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Digite o valor\nR$: '))
print('R${:.2f} --> US$ {:.2f}'.format(real, real / 5.31))
print('R${:.2f} --> EUR {:.2f}'.format(real, real / 5.52))
