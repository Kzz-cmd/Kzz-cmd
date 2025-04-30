def leiaint(num=0):
    while Exception:
        try:
            num = int(input('Digite um valor inteiro:\n'))
        except (TypeError,ValueError):
            print('Este valor não é inteiro')
        except KeyboardInterrupt:
            print('O usuário preferiu não responder, por isso, seu número inteiro é zero')
            return '0'
        else:
            return num
def leiafloat(num=0):
    while Exception:
        try:
            num = float(input('Digite um valor real:\n'))
        except (TypeError,ValueError):
            print('Este valor não é real')
        except KeyboardInterrupt:
            print('O usuário preferiu não responder, por isso, seu número real é zero')
            return '0'
        else:
            return num
print(f'O número inteiro digitado é {leiaint()} e o real é {leiafloat()}')
        

    
