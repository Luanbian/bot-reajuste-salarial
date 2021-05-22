# bot que calcula salario usando python

## Inicialmente ele te pergunta: "Hoje é dds ou fds?" 

dds significa Dia De Semana e a hora vale R$ 7.05

fds significa fim de semana ou feriados e a hora vale R$ 14.10

### estes valores podem ser alterados nas linhas 07 até a 10 
```python
#condiçoes do dia
if (dia == 'dds'):
    pago = 7.05
else:
    pago = 14.10
```
-----

### Após saber a data o aplicativo lhe pergunta que horas o trabalhador começou o trabalho e a que horas o terminou
*Lembrando que a resposta deve ser em formato de horas HH:MM*

A resposta serão as horas trabalhadas já subtraida 1h30 de almoço
E este valor de almoço pode ser alterado na linha 13
```python
time1 = datetime.strptime(fim, format) - datetime.strptime(inicio, format) - timedelta(hours=1, minutes=30)
```
----
## Também é calculado horas extras
### Por padrão se a quantidade de horas trabalhadas for maior do que 8h é considerado hora extra
#### E este valor também pode ser alterado na linha 20
```python
duracao2 = timedelta(hours=8, minutes=0, seconds=0)
```
Se o valor de horas trabalhadas for menor ou igual do que 8h, aparece na tela:
- [x] que não houve horas extras trabalhadas
- [x] o valor total a ser pago

Se o valor de horas trabalhadas for maior do que 8h, aparece na tela:
- [x] a quantidade de horas extras trabalhadas 
- [x] o valor a ser pago sem as horas extras
- [x] o valor a ser pago com as horas extras
- [x] o valor total a ser pago

