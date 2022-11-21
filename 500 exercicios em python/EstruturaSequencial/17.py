print ('outro programa para loja de tintas') 

tamanho = float(input ('Digitie o tamanho da parede em metros quadrados: ')) 

#1 litro da pra 6 metros
#18 litros 80 reais
#3,6 litros 25 reais
LitrosParede = tamanho * 6 
variavel = int(input('digite 1 para apenas galões de 18 litros, digite 2 para apenas galões de 3.6 litros e digite 3 para ambas as opções: '))
if variavel == 1:
#apenas galões normais
    if tamanho <=108: 
        print ('Você precisará comprar apenas 1 lata de tinta por R$80,00 ') 
    elif tamanho % 6 == 0: 
        print('Você precisará comprar: ', tamanho/108 ,' latas de tinta por', tamanho/108*80, 'reais')
    elif tamanho % 6 != 0:
        comprar1 = int (tamanho / 108) + (tamanho % 6 > 0)
        preco1 = float(comprar1*80)
        print ('Você precisará comprar ', comprar1, 'baldes de tintas por', preco1, 'reais') 
    else:
        print('não entendi nada queridão')
        input ('exit') 
elif variavel == 2:
#apenas galões de 3.6 litros 
    if tamanho <= 21.6:
        print('Você precisará comprar apenas 1 galão de tinta por R$25,00')
    elif tamanho % 21.6 == 0: 
        print('Você precisará comprar: ', tamanho/21.6 ,'galões de tinta por', tamanho/21.6*25, 'reais')
    elif tamanho % 21.6 != 0:
        comprar2 = int(tamanho / 21.6) + (tamanho%3.6>0)
        preco2 = float(comprar2*25)
        print('você precisará comprar ' ,comprar2, 'baldes de tinta por' , preco2, 'reais')
    else:
        input('exit')
elif variavel == 3:
#tudo junto
    if tamanho <= 21.6:
        print('Compre apenas 1 galão de 3.6 litros por R$25')
    elif tamanho <= 43.6:
        print('Compre apenas 2 galões de 3.6 litros por R$50')
    elif tamanho <= 64.8:
        print('Compre apenas 3 galões de 3.6 litros por R$75')
    elif tamanho <= 108:
        print('compre apenas 1 lata de 18 litros por R$80')
    else:
        total = int(tamanho/108) 
        resto = int(tamanho%108)
        resto_a = int(resto/21.6 + (resto%21.6>0))
        Dezporcento = tamanho%108
        if Dezporcento >= 20:

            print('Você precisará comprar: ', total, 'latas de tinta e ', resto_a+1, 'galões de tinta')
            valor2 = int(total*80) + int(resto_a*25)
            print('Valor a pagar: R$',valor2+25)
    
        else:
            print('Você precisará comprar: ', total, 'latas de tinta e ', resto_a, 'galões de tinta')
            valor2 = int(total*80) + int(resto_a*25)
            print('Valor a pagar: R$',valor2)
            input('exit')
else:
    input("exit")
input('exit')
    
    
    
    
    
    
    