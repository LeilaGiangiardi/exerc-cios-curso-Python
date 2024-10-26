#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
medida = float(input("Distância em metros: "))
cm = medida*100
#centimetro para metro multiplica por 100
mm = medida*1000
#milimetro para metro multiplica por 1000
print("{}m são:\n{}cm\n{}mm".format(medida, cm, mm))