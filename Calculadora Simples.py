from time import sleep
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
  
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)    
        numeros_validos = True
    except:
        numeros_validos = None
        
        if numeros_validos == None:
            print('Um ou ambos dos numeros digitados sao invalidos.')
            continue
        
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas 1 operador. ')
        
    print('Realizando sua conta. Confira o resultado abaixo:')    
    sleep(1)
        
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')
        
    sair = input('Deseja sair? sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break