# Relatório de Bugs

Este documento lista os bugs identificados no projeto, descreve os problemas, seu impacto e as soluções implementadas.

---

## **Bug 1: Função de soma retornando o resultado errado**

- **Descrição**: 
  A função `tangente` retorna o valor da soma errado, onde ele soma o x + (x,y).
  
- **Impacto**: 
  Resultados incorretos nas operações basicas

- **Causa**: 
  A função esta estruturada da forma incorreta

- **Correção**: 
  Antes de calcular a tangente, verificamos se o cosseno do ângulo é próximo de zero:
  ```python
    def adicao(x, y):
        return np.add(x, y)

## **Bug 2: Fatorial com resultado incorreto**

- **Descrição**: 
  A função `fatorial` retornava resultados incorretos devido a um loop mal estruturado.

- **Impacto**: 
  Resultados errados para números inteiros não negativos, prejudicando cálculos que dependam do fatorial.

- **Causa**: 
: O loop começava em 0, o que fazia o resultado final ser zero.

- **Correção**: 
  Ajustamos o loop para começar em 1:
  ```python
  for i in range(1, x + 1):
    fat *= i


## **Bug 3:  Erro no cálculo do logaritmo base 10 para números não positivos**

- **Descrição**: 
  A função `logaritmo_base10` permite valores inválidos como entrada (ex.: 0 ou negativos).
  
- **Impacto**: 
  Gera mensagens de erro ou resultados incorretos ao tentar calcular logaritmos de números inválidos.

- **Causa**: 
  A condição de validação da entrada (if x < 0) estava incorreta. Não considerava x == 0..

- **Correção**: 
  Ajustamos a condição para if x <= 0 e corrigimos o retorno:
  ```python
    def logaritmo_base10(x):
        if x <= 0:
            return "Erro: Logaritmo de número não positivo"
        return np.log10(x)


## **Bug 4: Funções Seno, Cosseno e Tangente não declaradas**

- **Descrição**: 
  As funções `seno, cosseno e tangente` não estavam declaradas no menu do código.
  
- **Impacto**: 
  Não conseguir executar as funcionalidades do seno, cosseno e tangente
  
- **Correção**: 
  Foi adicionado a lista de funções:
  ```python
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








