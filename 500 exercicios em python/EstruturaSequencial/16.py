print('Loja de tintas super legal')
area = float(input('Digitie a área da parede em metros quadrados: '))
lata = int(18)
if area <= 54:
	print('Para pintar a sua parede você precisará de apenas 1 lata de tinta')
	print('de 18 litros com o valor de R$ 80,00')
else:
	final2 = int(area/3/lata) + (area%3>0)
	if area % 54 == 0:
		preço = int(final2 * 80)
		print('o núemero de latas que você vai precisar é de:', final2 )
		print('e o preço que você vai ter que pagar é de ', preço )
	else:
		final2 + 1 
		preço = int(final2 * 80)
		print('o número de latas que você vai precisar é de:', final2 )
		print('e o preço que você vai ter que pagar é de ', preço )
input('exit')

