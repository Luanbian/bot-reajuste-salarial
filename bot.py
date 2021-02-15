from datetime import timedelta
from datetime import datetime, timedelta
dia = input('Hoje é dds ou fds? ')
inicio = input("Que horas ele começou o trabalho? ")
fim  = input("Que horas ele terminou o trabalho? ")
#condiçoes do dia
if (dia == 'dds'):
    pago = 7.05
else:
    pago = 14.10
#formato do datetime
format = '%H:%M'
time1 = datetime.strptime(fim, format) - datetime.strptime(inicio, format) - timedelta(hours=1, minutes=30)
print('horas trabalhadas: ')
print(time1)
print("pegue este valor e copie")
s = input("cole aqui ->")
horas, minutos, segundos = map(int, s.split(':'))
duracao1 = timedelta(hours=horas, minutes=minutos, seconds=segundos)
duracao2 = timedelta(hours=8, minutes=0, seconds=0)
nova_duracao5 = duracao1 * pago #este valor muda
#condições do dia
if (dia == 'fds'):
    nova_duracao1 = duracao1 * 14.10
    y = 0
else:
    print('')
#hora extra
if (duracao1 > duracao2 and dia == 'dds'):
   sub =(duracao1 - duracao2)
   print("Quantidade de horas extras: ")
   print(sub)
   x = input("coloque a quantidade de horas extras aqui ->")
   horas, minutos, segundos = map(int, x.split(':'))
   duracao3 = timedelta(hours=horas, minutes=minutos, seconds=segundos)
   nova_duracao1 = duracao3 * 10.58
   y = 56.4
   print('o valor que deve ser pago pelas horas extras: {:.2f}'.format(nova_duracao1.total_seconds() / 3600))
   print('o valor a ser pago sem as horas extras é: {:.2f}'.format(y))
#sem hora extra
if (duracao1 <= duracao2):
    print("não teve hora extra")
    valor = (nova_duracao5.total_seconds() / 3600)
    print('O valor a ser pago sem horas extras é: {:.2f}'.format(valor))
#escopo global
else:
    total = ((nova_duracao1.total_seconds() / 3600)) + y
    print('o valor TOTAL a ser pago é de: {:.2f}'.format(total))
#fim do código
input("aperte enter para fechar")
 

