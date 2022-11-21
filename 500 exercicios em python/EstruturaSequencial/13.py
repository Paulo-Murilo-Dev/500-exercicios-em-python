print('calcular o peso ideal para homens e mulheres')

v1 = str(input("Digite 'h' para homem e 'm' para mulher: "))
al = float(input('agora digite sua altura: '))

if v1 == 'h': 
	x = (al*72.7)-58
	print('o seu peso ideal é: ', x)
else:
	x = (al*62.1)-44.7
	print('o seu peso ideal é: ', x)
input('exit')