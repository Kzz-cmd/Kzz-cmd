a = float(input('Qual é o comprimento do lado do A do triângulo?\n'))
b = float(input('Qual é o comprimento do lado do B do triângulo?\n'))
c = float(input('Qual é o comprimento do lado do C do triângulo?\n'))

if a + b > c and b + c > a and c + a > b:
    print('Sim!!, isso é um triângulo')
else:
    print('Não, isso não é um triângulo em lugar nenhum')
