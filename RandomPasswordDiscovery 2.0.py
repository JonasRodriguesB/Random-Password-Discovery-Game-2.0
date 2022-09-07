import random
import time

senha_real = list()

num_digito = 0
while num_digito < 1 or num_digito > 4:
    try:
        num_digito = int(input("Quantos dígitos a senha deve conter, entre 1 e 4? "))
    except:
        print('Favor inserir apenas números, entre 1 e 4!')
print('Ótimo, vamos começar')
time.sleep(1)
print('Vou agora gerar uma senha que você deve descobrir qual é!')
time.sleep(1)
#Gera senha conforme o input do usuário
if num_digito == 1:
    senha_real.append(random.randint(0, 9))
    senha_nova = ['X']
elif num_digito == 2:
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_nova = ['X', 'X']
elif num_digito == 3:
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_nova = ['X', 'X', 'X']
else:
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_real.append(random.randint(0, 9))
    senha_nova = ['X', 'X', 'X', 'X']
time.sleep(1)
while senha_nova != senha_real:
    palpite = -1
    while palpite < 0 or palpite > 9:
        try:
            palpite = int(input('Insira um número entre 0 e 9 para começar a adivinhar a senha: '))
        except:
            print('Favor inserir apenas números entre 0 e 9')
    frequencia = senha_real.count(palpite)
    if frequencia == 0:
        print(f'A senha não contém nenhum número {palpite}')
    elif frequencia == 1:
        print(f'A senha contém um número {palpite} e está na posição {senha_real.index(palpite)+1}.')
        senha_nova.insert(senha_real.index(palpite), palpite)
        senha_nova.pop(senha_real.index(palpite) + 1)
    elif frequencia == 2:
        p1 = senha_real.index(palpite)
        p2 = senha_real.index(palpite, p1+1)
        print(f'A senha contém dois números {palpite} e estão nas posições {p1 + 1} e {p2 + 1}.')
        senha_nova.insert(p1, palpite)
        senha_nova.pop(p1 + 1)
        senha_nova.insert(p2, palpite)
        senha_nova.pop(p2 + 1)
    elif frequencia == 3:
        p1 = senha_real.index(palpite)
        p2 = senha_real.index(palpite, p1+1)
        p3 = senha_real.index(palpite, p2+1)
        print(f'A senha contém três números {palpite} e estão nas posições {p1 + 1}, {p2 + 1} e {p3 + 1}')
        senha_nova.insert(p1, palpite)
        senha_nova.pop(p1 + 1)
        senha_nova.insert(p2, palpite)
        senha_nova.pop(p2 + 1)
        senha_nova.insert(p3, palpite)
        senha_nova.pop(p3 + 1)
    else:
        p1 = senha_real.index(palpite)
        p2 = senha_real.index(palpite, p1+1)
        p3 = senha_real.index(palpite, p2+1)
        p4 = senha_real.index(palpite, p3+1)
        print(f'A senha contém quatro números {palpite} e estão nas posições {p1 + 1}, {p2 + 1}, {p3 + 1} e {p4 + 1}')
        senha_nova.insert(p1, palpite)
        senha_nova.pop(p1 + 1)
        senha_nova.insert(p2, palpite)
        senha_nova.pop(p2 + 1)
        senha_nova.insert(p3, palpite)
        senha_nova.pop(p3 + 1)
        senha_nova.insert(p4, palpite)
        senha_nova.pop(p4 + 1)
    time.sleep(1)
    if senha_real == senha_nova:
        time.sleep(1)
        print('Parabéns, você descobriu a senha!')

    #Imprime a senha conforme o número de dígitos
    print('== SENHA ==')
    if num_digito == 1:
        print(f'   = {senha_nova[0]} =    ')
    elif num_digito == 2:
        print(f'  = {senha_nova[0]} {senha_nova[1]} =  ')
    elif num_digito == 3:
        print(f' = {senha_nova[0]} {senha_nova[1]} {senha_nova[2]} = ')
    else:
        print(f'= {senha_nova[0]} {senha_nova[1]} {senha_nova[2]} {senha_nova[3]} =')
    print('===========')
    time.sleep(1)
