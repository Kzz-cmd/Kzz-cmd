#Importação do alfabeto
from string import ascii_lowercase

#Funções
def descriptografação(texto):
    '''Função que descriptografa um texto criptografado
    param: texto: str: texto criptografado
    return: str: texto descriptografado'''
    alfabeto = ascii_lowercase
    texto = texto.split(' - ')
    descriptografia = [alfabeto[int(indice) - 1] for indice in texto]
    return ''.join(descriptografia)

def criptografação(texto):
    '''Função que criptografa um texto
    param: texto: str: texto a ser criptografado
    return: str: texto criptografado'''

    alfabeto = ascii_lowercase
    texto = ''.join([letra for letra in str(texto).replace(' ','').lower() if letra in alfabeto])
    criptografia = [str(alfabeto.index(letra) + 1) for letra in texto]
    return ' - '.join(criptografia)

def fibonnaci(num):
    '''Função que retorna o n-ésimo termo da sequência de Fibonacci
    param: n: int: n-ésimo termo da sequência
    return: int: n-ésimo termo da sequência de Fibonacci'''
    if num <= 1:
        return num
    else:
        return (fibonnaci(num - 1) + fibonnaci(num - 2))

def remocao(frase,remocao):
    '''Função que remove uma série de letras de uma frase
    param: frase: str: frase a ser alterada
    param: remocao: str: caractere a ser removido
    return: str: frase alterada'''
    if remocao in frase:
        frase = frase.replace(remocao,'')
    return frase

def raio():
    '''Função que calcula a área de um círculo
    return: float: área do círculo'''
    r = float(input('Digite o raio do círculo: '))
    return 3.14 * r**2

def celsius():
    ''''Função que converte uma temperatura de Celsius para Fahrenheit'''
    c = float(input('Digite a temperatura em Celsius: '))
    return c * 1.8 + 32

# ...existing code...

def dividir_conta():
    '''Função que divide igualmente a conta da pizza entre todos e calcula o troco por pessoa'''
    valor_total = float(input('Digite o valor total da conta: '))
    numero_pessoas = int(input('Digite o número de pessoas no grupo: '))
    valor_cedula = float(input('Digite o valor da cédula de pagamento: '))
    
    valor_por_pessoa = valor_total / numero_pessoas
    troco_por_pessoa = valor_cedula - valor_por_pessoa
    
    print(f'Valor por pessoa: R$ {valor_por_pessoa:.2f}')
    print(f'Troco por pessoa: R$ {troco_por_pessoa:.2f}')

def media_ponderada():
    '''Função que calcula a média ponderada de 3 notas
    return: float: média ponderada'''
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    return (n1 * 2 + n2 * 3 + n3 * 5) / 10

def check_idade():
    '''Função que verifica se uma pessoa é maior de idade
    return: str: mensagem de maioridade'''
    idade = int(input('Digite a idade: '))
    return 'Maior de idade' if idade >= 18 else 'Menor de idade'

def sangue_elegivel():
    '''Função que verifica se uma pessoa pode doar sangue
    return: str: mensagem de elegibilidade'''
    anos = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    if anos >= 18 and anos <= 65 and peso >= 50:
        return 'Pode doar sangue'
    else:
        return 'Não pode doar sangue'

def aprov_concorso():
    '''Função que verifica se uma pessoa foi aprovada em um concurso
    return: str: mensagem de aprovação'''
    teorica = float(input('Digite a nota da prova teórica: '))
    pratica = float(input('Digite a nota da prova prática: '))
    return 'Aprovado' if teorica >= 60 and pratica >= 70 else 'Reprovado'

def par_impar():
    '''Função que verifica se um número é par ou ímpar
    return: str: mensagem de paridade'''
    num = int(input('Digite um número: '))
    return 'Par' if num % 2 == 0 else 'Ímpar'

def avaliacao():
    '''Função que avalia a situação de um funcionario
    return: str: mensagem de avaliação'''
    produtividade = int(input('Digite o salário: '))
    comportamento = int(input('Digite a nota de comportamento: '))
    if produtividade > 80 and comportamento > 90:
        return 'Excelente'
    elif produtividade < 80 and comportamento < 90:
        return 'Reprovado'
    else:
        return 'Bom'

def desconto():
    '''Função que calcula o desconto de uma compra
    return: float: valor da compra com desconto'''
    valor = float(input('Digite o valor da compra:\n'))
    if valor > 1000:
        valor = valor * 0.8
        return valor
    elif valor > 500:
        valor = valor * 0.9
        return valor
    else:
        return valor

def somente_pares():
    '''Uma função que solicita o um intervalo de números e retorna uma lista par
    return: list: lista de números pares no intervalo'''
    inicio = int(input('Digite o início do intervalo: '))
    fim = int(input('Digite o fim do intervalo: '))
    pares = [num for num in range(inicio,fim+1) if num % 2 == 0]
    return pares

def soma_acum():
    '''Função que calcula a soma acumulada de uma lista de números
    return: list: lista de somas acumuladas'''
    numero = 0
    acum = 0
    while True:
        numero = int(input('Digite um número:'))
        if numero >= 0:
            acum = acum + numero
        else:
            break
    return acum

def senha():
    '''Função que verifica a validade de uma senha
    return: resposta de acesso'''
    tentativa = ''
    while tentativa != '12345':
        tentativa = str(input('Digite a senha:'))
        if tentativa != '12345':
            print('Acesso Negado')
    return 'Acesso Permitido'

def mult3():
    '''Função que conta quantos números no intervalo recebido são múltiplos de 3.
    return: lista com números múltiplos de 3'''
    inicio =  int(input('Digite o inicio: '))
    fim = int(input('Digite o fim: '))
    multi3 = [num for num in range(inicio,fim) if num % 3 == 0]
    return len(multi3)

def idades():
    '''Função que calcula a média de adultos
    return: media'''
    idade = 1
    acum = quantia = 0
    while idade != 0:
        idade = int(input('Digite sua idade: '))
        if idade >= 18:
            acum = acum + idade
            quantia = quantia + 1
    return acum/quantia