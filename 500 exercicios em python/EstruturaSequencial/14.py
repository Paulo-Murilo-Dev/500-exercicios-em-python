print('calcular peso-pexe 2000')
peso = int(input('Digite quantos kilos de peixe você pescou hoje: '))

if peso <= 50:
	print('não há taxas para serem pagas')
else:
	taxa = (peso-50)*4
	print('Há um total de: ',taxa, 'reais em impostos a serem pagos') 
input('exit')
