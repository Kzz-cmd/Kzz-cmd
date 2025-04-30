peso = float(input('Digite o seu peso:\n'))
alt = float(input('Digite sua altura:\n'))

imc = peso/alt**2

print (imc)
if imc < 18.5:
    print('Você é abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você tem um peso ideal')
elif imc >= 25 and imc < 30:
    print('Você é sobrepeso')
elif imc >=30 and imc <= 40:
    print('Você é obeso')
else:
    print('Você tem obesidade mórbida')
