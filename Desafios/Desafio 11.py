# Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg, altura = float(input('Largura: ')), float(input('Altura: '))
area = larg*altura
print('Área:{:.1f}m²'.format(area))
print('Tinta necessária:{}l'.format(area/2))
