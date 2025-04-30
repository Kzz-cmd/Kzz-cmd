#Definição da função

def notas(*num,situacao=False):

    #Declaração do dicionário de armazenamento de números
    
    dic = {}

    #Definição de chaves do dicionário

    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['média'] = sum(num)/len(num)
    
    #Estrutura condicional de definição de situação do aluno

    if situacao == False:
        pass
    else:
        if dic['média'] >= 7:
            dic['situacao'] = 'Aprovado'
        elif dic['média'] <= 4:
            dic['situacao'] = 'Reprovado'
        else:
            dic['situacao'] = 'Prova Final'

    #Retorno do dicionário

    return dic

#Impressão dos resultados e uso da função

print(notas(10,5.5,8.5,6.9,8.0,situacao=True))