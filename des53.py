pal = str(input('Digite uma palavra:\n')).lower().replace('ó','o').replace('á','a').replace('é','e').replace('í','i').replace('ú','u')

indr = pal[::-1]

if pal.replace(" ","") == indr.replace(" ",""):
    print('Essa palavra/frase é um palíndromo')
else:
    print('Essa palavra/frase não é um palíndromo')
