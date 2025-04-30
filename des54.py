from datetime import date
dmaior = 0
dmenor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa:\n'.format(c)))
    idade = date.today().year - ano
    if idade >= 18 :
        dmaior = dmaior + 1
    else:
        dmenor = dmenor + 1
print('Das 7 pessoas presentes {} são maiores de 18 anos e {} são menores'.format(dmaior, dmenor))
    
        
