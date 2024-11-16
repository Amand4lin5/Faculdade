# Projeto Faculdade

Este repositpório é projetado para o desenvolvimento da atividade da **matéria - Alta Qualidade de Software** Trazendo a resolução da **Parada Obrigatória 2**

## Descrição

Este projeto tem como objetivo fazer a identificação e resolução dos bugs presentes no código da calculadora fornecido pelo professor, onde a gente realize a identificação dos bugs, corrija eles, executem os testes e crie um relatório

## Estrutura do Repositório

- `parada_obrigatoria2/`: Contém os bugs identificados, os requirements, além das pastas docs, src, tests.
- `docs/`: Contém o relatorio de bugs.
- `src/`: Contém o código corrigido.
- `docs/`: Contém os testes que foram realizados.

## Tecnologias Utilizadas

- Linguagem: Python

## Como Rodar o Projeto

### Passos

1. **Clone o repositório**:

    ```bash
# Clone o repositório sem fazer checkout imediato
git clone --no-checkout https://github.com/Amand4lin5/Faculdade.git

# Entre no repositório
cd Faculdade

# Habilite o sparse-checkout
git sparse-checkout init --cone

# Defina o diretório que você quer clonar
git sparse-checkout set paradaobrigatoria2

# Faça checkout para obter a pasta
git checkout main  # ou o nome do branch desejado
    ```

2. **Instale as dependências**:

  Instale as dependências presentes no arquivo requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

3. **Vá ao diretório do código atualizado**:

    ```bash
    cd ./src
    ```

4. **Execute**:

  Execute o código e teste a calculadora de uma forma corrigida
  
  ```bash
      python Calculadora.py
  ```


