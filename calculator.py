import os
def limpar_tela():
    os.system('cls')

def soma(x,y):
    calculo=x+y
    print(f'{x}+{y}={calculo:.1f}')

def sub(x,y):
    calculo=x-y
    print(f'{x}-{y}={calculo:.1f}')

def mult(x,y):
    calculo=x*y
    print(f'{x}X{y}={calculo:.1f}')

def div(x,y):
    calculo=x/y
    print(f'{x}÷{y}={calculo:.1f}')

def get_num():
    x1=float(input('Digite o primeiro número para a realizar a  peração:').replace(',','.'))
    x2=float(input('Digite o segundo número para a realizar a  peração:'.replace(',','.')))
    return x1,x2

def retornar():
    while True:
        prox=str(input('Pressione \033[1;33m[ENTER]\033[0m para realizar outra operação'))
        if prox!='':
            continue
        else:
            limpar_tela()
            break


while True:
    limpar_tela()
    print('\033[1;34mBem-vindo a calculadora\033[0m')
    escolha=str(input('Pressione \033[1;33m[ENTER]\033[0m para continuar:'))
    if escolha!='':
        continue
    else:
        break


while True:
    limpar_tela()
    print('Escolha uma operação ou digite \033[1;31mSair\033[0m para finalizar o programa.')
    print('1-Soma')
    print('2-Subtração')
    print('3-Mutiplicasão')
    print('4-Divisão')
    escolha=str(input('Qual a sua escolha:'))
    escolha=escolha.lower()
    if escolha=='1':
        n1,n2=get_num()
        soma(n1,n2)
        retornar()
    elif escolha=='2':
        n1,n2=get_num()
        sub(n1,n2)
        retornar()
    elif escolha=='3':
        n1,n2=get_num()
        mult(n1,n2)
        retornar()
    elif escolha=='4':
        n1,n2=get_num()
        div(n1,n2)
        retornar()
    elif 'sair'in escolha:
        print('\033[1;32mObrigado por utilizar a calculadora :)\033[0m')
        break
    else:
        limpar_tela()
        print('\033[1;31mERRO\033[0m:Comando invalido!')