import numpy as np

def adicao(x, y):
    return np.add(x, y)

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return np.multiply(x, y)

def divisao(x, y):
    return x / y

def potencia(x, y):
    return np.power(x, y)

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo"
    return np.sqrt(x)

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo"
    fat = 1
    for i in range(1, x + 1): 
        fat *= i
    return fat

def logaritmo_natural(x):
    if x <= 0:
        return "Erro: Logaritmo de número não positivo"
    return np.log(x)  

def logaritmo_base10(x):
    if x <= 0: 
        return "Erro: Logaritmo de número não positivo"
    return np.log10(x) 

def seno(x, radianos=True):
    if not radianos:
        x = np.radians(x) 
    return np.sin(x)

def cosseno(x, radianos=True):
    if not radianos:
        x = np.radians(x)
    return np.cos(x)

def tangente(x, radianos=True):
    if not radianos:
        x = np.radians(x)
    if np.isclose(np.cos(x), 0, atol=1e-9):
        return "Erro: Tangente indefinida para este ângulo"
    
    return np.tan(x)

def menu():
    print("Bem-vindo à Calculadora Científica")
    print("Escolha a operação que deseja realizar:")
    print("0. Sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Logaritmo Natural (ln)")
    print("9. Logaritmo Base 10")
    print("10. Seno")
    print("11. Cosseno")
    print("12. Tangente")

def calculadora_cientifica():
    def obter_entrada(mensagem, tipo=float):
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            return obter_entrada(mensagem, tipo)
    
    menu()
    escolha = input("Digite o número da operação: ")
    
    # Operações binárias: necessitam de dois números
    operacoes_binarias = {
        '1': ("Adição", adicao),
        '2': ("Subtração", subtracao),
        '3': ("Multiplicação", multiplicacao),
        '4': ("Divisão", divisao),
        '5': ("Potenciação", potencia)
    }

    # Operações unárias: necessitam de um número
    operacoes_unarias = {
        '6': ("Raiz Quadrada", raiz_quadrada),
        '7': ("Fatorial", lambda x: fatorial(int(x))),
        '8': ("Logaritmo Natural (ln)", logaritmo_natural),
        '9': ("Logaritmo Base 10", logaritmo_base10),
        '10': ("Seno", lambda x: seno(x, radianos=False)),
        '11': ("Cosseno", lambda x: cosseno(x, radianos=False)),
        '12': ("Tangente", lambda x: tangente(x, radianos=False))
    }

    if escolha == '0':
        print("Calculadora encerrada.")
        return

    if escolha in operacoes_binarias:
        x = obter_entrada("Digite o primeiro número: ")
        y = obter_entrada("Digite o segundo número: ")
        nome, funcao = operacoes_binarias[escolha]
        print(f"Resultado ({nome}):", funcao(x, y))
    
    elif escolha in operacoes_unarias:
        x = obter_entrada("Digite o número: ")
        nome, funcao = operacoes_unarias[escolha]
        print(f"Resultado ({nome}):", funcao(x))
    
    else:
        print("Operação inválida. Tente novamente.")
    
    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar == 's':
        calculadora_cientifica()

calculadora_cientifica()
