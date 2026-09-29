# Documentação Técnica: Conversor de Moedas
## 1. Descrição da Funcionalidade

O Conversor de Moedas é uma aplicação que permite ao usuário converter valores entre diferentes moedas pré-definidas (por exemplo, USD, EUR, BRL). A aplicação fornece uma interface gráfica onde o usuário pode selecionar a moeda de origem, a moeda de destino, inserir a quantidade a ser convertida e, em seguida, receber o valor convertido. A conversão é realizada com base em taxas de câmbio pré-definidas no backend.

### Funcionalidades principais:
1. Seleção da moeda de origem e moeda de destino.
2. Inserção da quantidade de moeda a ser convertida.
3. Exibição do valor convertido em tempo real na própria interface.

# Diagrama de Fluxo
O diagrama de fluxo a seguir descreve a sequência de interações entre o cliente (navegador) e o servidor (FastAPI):

![image](https://github.com/user-attachments/assets/838bd510-f2d8-476e-a25f-97a2612e55c5)


### Passos:
O usuário seleciona as moedas e insere a quantidade na interface.
Ao submeter o formulário, a função JavaScript intercepta o envio e faz uma requisição assíncrona (AJAX) ao servidor FastAPI.
A API FastAPI processa a requisição, realiza a conversão e retorna o valor convertido em JSON.
O JavaScript exibe o resultado na interface sem a necessidade de recarregar a página.

# Interfaces Necessárias
### Interface de Usuário (HTML + JavaScript)
A interface do usuário é construída em HTML, com JavaScript responsável por manipular a submissão assíncrona dos dados e a exibição dos resultados.

Componentes principais:
Formulário HTML: Contém os campos de seleção de moeda de origem, moeda de destino e quantidade.
Função JavaScript (AJAX): Envia uma requisição POST para o servidor com os dados do formulário e atualiza a interface com o resultado.
**Exemplo de formulário:**

~~~~shell
<form onsubmit="convertCurrency(event)">
    <label for="from_currency">Selecione a moeda de origem:</label>
    <select name="from_currency" id="from_currency" required>
        <!-- Opções de moedas geradas dinamicamente -->
    </select>

    <label for="to_currency">Selecione a moeda de destino:</label>
    <select name="to_currency" id="to_currency" required>
        <!-- Opções de moedas geradas dinamicamente -->
    </select>

    <label for="amount">Quantidade:</label>
    <input type="number" name="amount" id="amount" step="0.01" required>

    <button type="submit">Converter</button>
</form>

<!-- Resultado da conversão exibido aqui -->
<div id="result"></div>
~~~~


### API FastAPI
O backend da aplicação utiliza FastAPI para processar as requisições de conversão.

Rota Principal (/): Serve a interface HTML com as opções de moedas.
Rota de Conversão (/convert/): Processa a requisição POST contendo os dados (moeda de origem, moeda de destino e quantidade) e retorna o valor convertido no formato JSON.


# Banco de Dados ou Detalhes de Armazenamento
Este projeto não utiliza um banco de dados propriamente dito. As taxas de câmbio são armazenadas diretamente em um dicionário Python, o que simplifica o processo e reduz a complexidade de integração com um sistema de banco de dados. O dicionário é estático e pode ser facilmente atualizado conforme necessário.

Exemplo de dicionário de taxas de câmbio:

~~~~shell
exchange_rates = {
    "USD": 1.0,     # Dólar dos EUA
    "EUR": 0.85,    # Euro
    "BRL": 5.25     # Real Brasileiro
}

~~~~

As taxas de câmbio são utilizadas diretamente para o cálculo de conversão, sem a necessidade de consultas a um banco de dados.


# APIs ou Serviços Externos Envolvidos
### FastAPI
FastAPI é o principal framework utilizado no backend para criação de rotas e processamento de requisições. Ele fornece endpoints RESTful que lidam com as operações de conversão de moedas.

Rota /convert/: Processa requisições POST e retorna o valor convertido com base nas taxas de câmbio armazenadas localmente. A função que processa o pedido é semelhante ao seguinte:

~~~~shell
@app.post("/convert/")
async def convert_currency(
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return {"error": "Moeda não suportada."}

    # Cálculo da conversão
    converted_amount = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]
    
    return {"converted_amount": round(converted_amount, 2), "currency": to_currency}
~~~~

### JavaScript (AJAX)
A interação entre a interface de usuário e a API FastAPI é realizada com o auxílio de JavaScript, através de requisições AJAX. Isso permite que os dados sejam enviados ao servidor sem recarregar a página, tornando a experiência do usuário mais fluida.

Exemplo de função JavaScript que faz a requisição:


~~~~shell
function convertCurrency(event) {
    event.preventDefault();
    const fromCurrency = document.getElementById("from_currency").value;
    const toCurrency = document.getElementById("to_currency").value;
    const amount = document.getElementById("amount").value;

    fetch("/convert/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
            "from_currency": fromCurrency,
            "to_currency": toCurrency,
            "amount": amount
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent = `Valor Convertido: ${data.converted_amount} ${data.currency}`;
    });
}
~~~~



# Considerações Finais
A aplicação de conversor de moedas foi projetada para ser simples, eficiente e amigável ao usuário. A utilização de FastAPI no backend, juntamente com JavaScript no frontend, garante que a aplicação funcione de maneira assíncrona e responsiva.

Possíveis Melhorias Futuras:
Integração com uma API externa de câmbio para obter taxas de conversão em tempo real.
Implementação de testes automatizados para validação das funcionalidades.
Inclusão de mais moedas na lista de opções para conversão.
