#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Preço do produto em R$: '))
desconto = preço - (preço*5/100)
print('Com desconto de 5% o produto custará R${:.2f}'.format(desconto))