print('calculadora de impostos')

salarioh = int(input('Digite o quanto você ganha por hora trabalhada: '))
tempo = int(input('Agora digite o núemero de horas trabalhadas no mês: '))

salario_bruto = salarioh*tempo
ir=(salario_bruto*11)/100
inss=(ir*8)/100
sindicato=(ir*5)/100
salario_liquido = salario_bruto-sindicato-inss-ir
print('R$',salario_bruto)
print('IR (11%): ', ir,'$')
print('INSS (8%): ', inss,'$')
print('Sindicato (5%): ', sindicato,'$')
print('salário líquido: ', salario_liquido,'$')
input('exit')

