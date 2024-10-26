#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input("Digite um número: "))
for a in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(n, a, a*n))