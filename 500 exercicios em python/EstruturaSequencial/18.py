print('Speed test')

Velocidade = int(input('Digite a velocidade da sua internet: '))
Tamanho = int(input('digite o tamanho do arquivo a ser baixado: '))

resultado_em_segundos = Tamanho/Velocidade
if resultado_em_segundos <= 60:
	segundos = resultado_em_segundos
	resultado_em_segundos=0
	print('O tempo aproximado será de: ',resultado_em_segundos,' mintos e: ',segundos,' segundos')
	input('exit')
else:
	minutos = int(resultado_em_segundos/60)
	segundos = int(resultado_em_segundos%60)
	print('O tempo aproximado será de: ',minutos,' mintos e: ',segundos,' segundos')
	input('exit')