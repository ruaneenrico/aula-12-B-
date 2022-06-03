qtde = int(input('informe quantos cigarros voce fuma por dia: '))

anos = int(input('informe por quantos anos voce fuma: '))


soma = qtde*(anos*365)
minutos = soma*18

subtrai = (minutos/60)/24

print('voce tem %.2f dias a menos de vida'%subtrai)











#--------------------------------#----------------------#------------------------#
print('---calculadora de dias de carro alugado-----')

d = int(input('quantos dias o carro ficou alugado: '))
k = float(input(' quantos km foram rodados: ').replace(',','.'))

paga=(d*60)+(k*0.15)

print('o valor a ser pago e R${:.2f} devido a {:.0f} dia de aluguel e{:.0f} km rodados'.format(paga,d,k))



#------------------#------------------------#--------------------------#
print('----conversor temperatura celsius para fahrenheit---')
c = float(input('insira a temperatura em celsius: ').replace(',','.'))
f = (9*(c/5)+32)
print('fahrenheit : {:2f}'.format(f))
print('\n\n----conversor temperatura fahrenhait para celsius----')
f = float(input('insira a temperatura em fahrenheit : ').replace(',','.'))
C = ((f-32)/1.8)