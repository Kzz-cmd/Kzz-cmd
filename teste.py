#Importação do alfabeto
from string import ascii_lowercase
from functools import reduce
from math import trunc,gcd,sqrt
from random import shuffle,choice,randint

#Funções
def correcao(pergunta,tipo=str):
    '''Tratamento de entradas do usuário
    param: pergunta: str: A pergunta a ser feita para o usuário
    param: tipo: Definição do tipo que é esperado
    return: Resposta da pergunta'''
    while Exception:
        try:
            pergunta = tipo(input(pergunta))
        except ValueError:
            print('Tipo errado')
        else:
            return pergunta

def divisao_de_lista(lista):
    '''Divide cada elemento de uma lista entre si
    param: list: lista: A lista a ser dividida
    return: int: Divisão da lista por completo'''
    return reduce(lambda a,b:a/b,lista)

def multiplicacao_de_lista(lista):
    '''Multiplica cada elemento de uma lista entre os própios números
    param: list: lista: A lista a ser multiplicada
    return: int: Multiplicação de uma lista por completo'''
    return reduce(lambda a,b:a*b,lista)

def descriptografaçao(texto):
    '''Função que descriptografa um texto criptografado
    param: texto: str: texto criptografado
    return: str: texto descriptografado'''
    alfabeto = ascii_lowercase
    descriptografia = [alfabeto[int(indice) - 1] for indice in texto.split(' - ')]
    return ''.join(descriptografia)

def criptografaçao(texto):
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
        return fibonnaci(num - 1) + fibonnaci(num - 2)

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
    rai = correcao('Digite o raio do círculo: ',float)
    return 3.14 * rai**2

def celsius():
    ''''Função que converte uma temperatura de Celsius para Fahrenheit
    return: float: Celsius convertido para Fahrenheit'''
    cel = correcao('Digite a temperatura em Celsius: ',float)
    return cel * 1.8 + 32 

def dividir_conta():
    '''Função que divide igualmente a conta da pizza entre todos e calcula o troco por pessoa'''
    valor_total = correcao('Digite o valor total da conta: ',float)
    numero_pessoas = correcao('Digite o número de pessoas no grupo: ',int)
    valor_cedula = correcao('Digite o valor da cédula de pagamento: ',float)
    
    valor_por_pessoa = valor_total / numero_pessoas
    troco_por_pessoa = valor_cedula - valor_por_pessoa
    
    print(f'Valor por pessoa: R$ {valor_por_pessoa:.2f}')
    print(f'Troco por pessoa: R$ {troco_por_pessoa:.2f}')

def check_idade():
    '''Função que verifica se uma pessoa é maior de idade
    return: str: mensagem de maioridade'''
    idade = correcao('Digite a sua idade: ',int)
    return 'Maior de idade' if idade >= 18 else 'Menor de idade'

def sangue_elegivel():
    '''Função que verifica se uma pessoa pode doar sangue
    return: str: mensagem de elegibilidade'''
    anos = correcao('Digite a idade: ',int)
    peso = correcao('Digite o peso: ',float)
    return 'Pode doar sangue' if anos >= 18 and anos <= 65 and peso >= 50 else 'Não pode doar sangue'

def aprov_concurso():
    '''Função que verifica se uma pessoa foi aprovada em um concurso
    return: str: mensagem de situação
    Aprovado se teorica >= 60 e pratica >= 70 senão Reprovado'''
    teorica = correcao('Digite a sua nota da prova teórica: ',float)
    pratica = correcao('Digite a nota da prova prática: ',float)
    return 'Aprovado' if teorica >= 60 and pratica >= 70 else 'Reprovado'

def par_impar(num):
    '''Função que verifica se um número é par ou ímpar
    return: bool: mensagem de paridade'''
    return True if num % 2 == 0 else False

def avaliacao():
    '''Função que avalia a situação de um funcionario
    return: str: mensagem de avaliação'''
    produtividade = correcao('Digite o salário: ',int)
    comportamento = correcao('Digite a nota de comportamento: ',int)
    if produtividade > 80 and comportamento > 90:
        return 'Excelente'
    elif produtividade < 80 and comportamento < 90:
        return 'Reprovado'
    else:
        return 'Bom'

def desconto():
    '''Função que calcula o desconto de uma compra
    return: float: valor da compra com desconto'''
    valor = correcao('Digite o valor da compra:\n',float)
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
    inicio = correcao('Digite o início do intervalo: ',int)
    fim = correcao('Digite o fim do intervalo: ',int)
    pares = [num for num in range(inicio,fim+1) if num % 2 == 0]
    return pares

def soma_acum():
    '''Função que calcula a soma acumulada de uma lista de números
    return: list: lista de somas acumuladas'''
    numero = acum = 0
    while True:
        numero = correcao('Digite um número:',int)
        if numero >= 0:
            acum = acum + numero
        else:
            break
    return acum

def senha():
    '''Função que verifica a validade de uma senha
    return: str: resposta de acesso'''
    tentativa = ''
    while tentativa != '12345':
        tentativa = correcao('Digite a senha:')
        if tentativa != '12345':
            print('Acesso Negado')
    return 'Acesso Permitido'

def multn(numero,quantia=False):
    '''Função que conta quantos números no intervalo recebido são múltiplos de um numero n fornecido na função.
    return: int: tamanho da lista com números múltiplos de 3'''
    inicio = correcao('Digite o início do intervalo: ',int)
    fim = correcao('Digite o fim do intervalo: ',int)
    multin = [num for num in range(inicio,fim) if num % numero == 0]
    if quantia:
        return len(multin)
    else:
        return multin

def idades():
    '''Função que calcula a média de adultos
    return: int/str: media de adultos'''
    idade = quantia = acum = 0
    while idade != 0:
        idade = correcao('Digite sua idade: ',int)
        if idade >= 18:
            acum = acum + idade
            quantia = quantia + 1
    return 'Não há adultos' if quantia == 0 else acum/quantia

def conversor_segundos(hora):
    ''''Função que converte um valor de horas, minutos em segundos
    param: hora: str: valor de horas, minutos e segundos
    obs: hora deve ser no formato 'h:m:s'
    return: int: valor em segundos'''
    hora = [trunc(float(tempo)) for tempo in hora.split(':')]
    return hora[0] * 3600 + hora[1] * 60 + hora[2]

def conversor_tempo(segundos):
    '''Função que converte um valor de segundos em horas, minutos e segundos
    param: segundos: int: valor em segundos
    return: str: valor em horas, minutos e segundos'''
    hora = segundos//3600
    minuto = (segundos % 3600)//60
    seg = (segundos % 3600) % 60
    return f'{hora}:{minuto}:{seg}'

def conversor_minutos(hora):
    '''''Função que converte um valor de horas em minutos
    param: hora: str: valor de horas, deve ser no formato 'h:m:s
    return: int: valor em minutos e segundos'''
    hora = [int(tempo) for tempo in hora.split(':')]
    return hora[0] * 60 + hora[1]

def fatorial(num):
    ''''Função que calcula o fatorial de um número
    param: num: int: número a ser calculado o fatorial
    return: int: fatorial do numero'''
    for c in range(1,num):
        num = num * c
    return num

def anagrama(palavra):
    '''Função que retorna anagrama da mesma palavra
    param: palavra: str: palavra a ser usada de exemplo
    return: str: anagrama da mesma palavra'''
    palavra = [letras for letras in palavra]
    shuffle(palavra)
    return ''.join(palavra)

def relogio():
    '''Função que escolhe um alien aleatório
    return: str: Um alien '''
    aliens = ['Chama','Cipó Selvagem','Besta','Massa Cinzenta','Aquático','XLR8','Insectoide','4 Braços','Fantasmático','Bola de Canhão','Frankinstrike','Pidão']
    print('É hora de virar Herói')
    return f'{choice(aliens)} eu escolho você'

def revanche(quantia):
    '''Recebe um número de notas de alunos, retornando a média desconsiderando a maior e menor nota
    param: quantia: int: quantia de notas que serão recebidas
    return: float: média das notas, desconsiderando a maior e a menor'''
    notas = [correcao(f'Digite a {c + 1}ª nota:\n',float) for c in range(int(quantia))]
    return (sum(notas) - (max(notas) + min(notas)))/(quantia - 2)

def assasino():
    '''Faz uma série de perguntas ao usuário
    return: Diz oque quem está respondendo as perguntas é'''

    perguntas = ['Conhecia a vítima?','Estava no local do assasinato?','?','?','Cometeu o assasinato??']
    acum = 0

    def questionamento(texto):
        '''Faz uma pergunta para o usuário
        return: int: retorna 1 se for escrito 'sim' senão 0'''
        resposta = correcao(texto + '\n',str)
        return 1 if resposta.lower() == 'sim' else 0

    for questoes in perguntas:
        acum = questionamento(questoes) + acum
    if acum < 3:
        return 'Inocente'
    elif acum > 3:
        return 'Assasino'
    else:
        return 'Cúmplice'

def adivinhacao():
    '''Sorteia um número entre 1 e 100 e pede para que o usuário adivinhe'''
    num = randint(1,100)
    for c in range(9,-1,-1):
        tentativa = correcao('Tente um número entre 1 e 100:',int) 
        if tentativa == num:
            print('Você acertou :D')
            break
        else:
            print('O número adivinhado pelo usuário é maior' if tentativa > num else 'O número adivinhado pelo usuário é menor')
            print(f'{c} Tentativas restantes')
    else:
        print(f'Você perdeu :(, o número correto era {num}')

def cesar(mensagem, deslocamento):
    '''Criptografa um texto através da criptografia de cesar
    param: mensagem: str: Oque deve ser criptografado
    param: deslocamento: int: O deslocamento que deve ser feito
    return: cript: str: versão criptografada da mensagem'''
    cript = ''
    alfabeto = ascii_lowercase
    try:
        cript = ''.join([alfabeto[alfabeto.index(letras) + deslocamento] for letras in mensagem])
    except IndexError:
        cript = ''.join([alfabeto[(alfabeto.index(letras) + (deslocamento % 26)) % 26] for letras in mensagem])
    finally:
        return cript

def antcesar(mensagem,deslocamento):
    '''Descriptografa um texto através da criptografia de cesar
    param: mensagem: str: Oque deve ser descriptografado
    param: deslocamento: int: O deslocamento que deve ser feito
    return: descript: str: versão descriptografada da mensagem'''
    descript = ''
    alfabeto = ascii_lowercase
    try:
        descript = ''.join([alfabeto[alfabeto.index(letras) - deslocamento] for letras in mensagem])
    except IndexError:
        descript = ''.join([alfabeto[(alfabeto.index(letras) - (deslocamento % 26)) % 26] for letras in mensagem])
    finally:
        return descript

def palindromo(palavra):
    '''Checa se uma palavra possuí a caracterisca de um palíndromo
    param: palavra: str: Palavra a ser checada
    return: bool: Verdadeiro para caso a palavra seja um palíndromo, senão false'''
    return True if palavra == palavra[::-1] else False

def mmc(numeros):
    '''Calcula o mínimo múltiplo comum de n números se a lista
    possuir mais de 2 números
    param: numeros: uma lista de números'''
    if len(numeros) < 2:
        return 'A lista possui apenas 1 número'
    else:
        formula = lambda a,b:abs(a * b)//gcd(a,b)
        return reduce(formula,numeros)

def remocao_de_acentos(frase):
    '''Remove acentos de vogáis
    param: str: frase: Frase a ter os acentos removidos
    return: str: Frase com acentos removidos'''
    for letras in 'áàãâäéèêëíìîïóòõôöúùûü':
        if letras in frase.lower():
            frase = frase.replace(letras,'a' if letras in 'áàãâä' else 'e' if letras in 'éèêë' else 'i' if letras in 'íìîï' else 'o' if letras in 'óòõôö' else 'u')
    return frase

def contador_vogais(palavras):
    '''Conta as vogais em uma frase fornecida
    param: palavras: str: Frase usada para contar as vogais
    return: contador_vogais: int: Quantia de vogais na frase'''
    contador_vogais = 0
    for letras in remocao_de_acentos(palavras).lower():
        if letras in 'aeiou':
            contador_vogais = contador_vogais + 1
    return contador_vogais

def graficos(formula,inicio=-3,fim=3):
    '''Revela o gráfico de uma função
    param: formula: str: Formula a ser usada para o gráfico (lambda)
    return: list: lista: Lista de números do gráfico'''
    lista = []
    for x in range(inicio,fim + 1):
        try:
            lista.append(formula(x))
        except ZeroDivisionError:
            lista.append(0)
        else:
            pass
    return lista

def transposição_de_matriz(matriz):
    '''Transpõe uma matriz
    param: matriz: list''
    return: list: matriz transposta'''
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def contador_letras(palavra):
    '''Diz a quantia de letras e uma palavra ou frase
    param: palavra: str: palavra ou frase
    '''
    print(f'A frase/palavra {palavra}')
    dicio = {}
    for letras in palavra:
        dicio[letras] = palavra.count(letras) 
    return dicio

def media(notas):
    '''Função que calcula a média de uma lista de notas
    param: notas: list: lista de notas
    return: float: média das notas'''
    return sum(notas)/len(notas)

def variancia(lista):
    '''Calcula a variância de uma lista forncida pelo usuário
    param: lista: list: A lista de elementos que será usada para calcular
    return: float: variância da lista fornecida'''
    acumulador = 0
    media_local = media(lista)
    for numeros in lista:
        acumulador = acumulador + (numeros - media_local)**2
    return acumulador/len(lista)

def desvio_padrao(lista):
    '''Calcula o desvio padrão de uma lista fornecida pelo usuário
    param: lista: list: A lista de elementos que será usada para calcular
    return: float: desvio padrão da lista fornecida'''
    return sqrt(variancia(lista))

def media_ponderada(lista,pesos):
    '''Função que calcula a média ponderada de uma lista
    param: lista: list: lista de notas
    param: pesos: list: lista de pesos
    return: float: média ponderada da lista com os pesos'''
    return sum(c * d for c,d in zip(lista,pesos))/sum(pesos) if len(lista) == len(pesos) else None
