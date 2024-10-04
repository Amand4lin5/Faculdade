# Tutorial: Como rodar o código da API de Conversor de Moedas

Este tutorial irá te guiar através do processo de configuração e execução da API de conversão de moedas utilizando FastAPI. Ao seguir os passos abaixo, você será capaz de rodar a API localmente e realizar conversões entre moedas.

### Requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados:

1.Python 3.8+
2.pip (gerenciador de pacotes Python)
3.FastAPI e Uvicorn (servidor ASGI para rodar a API)
4.Um ambiente virtual (opcional, mas recomendado)

## Passo 1: Clonar o Repositório
1.Clone o repositório que contém o código da API. Abra o terminal e execute o comando abaixo:

~~~~shell
docker compose up -d
~~~~

2.Navegue para o diretório do projeto:
~~~~shell
docker compose up -d
~~~~


## Passo 2: Criar um Ambiente Virtual (Opcional)
É uma boa prática isolar suas dependências de projeto dentro de um ambiente virtual.

1.Crie um ambiente virtual com o seguinte comando:
~~~~shell
python -m venv env
~~~~

2.Ative o ambiente virtual:
  
  **No Windows:**
  ~~~~shell
  .\env\Scripts\activate
  ~~~~


  **No macOS/Linux:**
  ~~~~shell
  source env/bin/activate
  ~~~~

## Passo 3: Instalar as Dependências
~~~~shell
pip install fastapi uvicorn
~~~~


## Passo 4: Rodar a API
Agora que as dependências estão instaladas, você pode rodar a API localmente com o Uvicorn. No diretório do projeto, execute o seguinte comando:
~~~~shell
uvicorn main:app --reload
~~~~
Aqui:
  1.main é o nome do arquivo Python que contém a instância da sua aplicação FastAPI (app).
  2.O parâmetro --reload ativa o recarregamento automático sempre que há mudanças no código.

  
## Passo 5: Acessar a API
Após rodar o comando acima, a API estará disponível localmente no endereço:
~~~~shell
http://127.0.0.1:8000
~~~~

## Passo 6: Testar a API
1.Acesse o navegador e navegue até a documentação interativa gerada automaticamente pelo FastAPI no seguinte link:
~~~~shell
http://127.0.0.1:8000/docs
~~~~

2.A interface Swagger UI será exibida, permitindo que você teste a conversão de moedas diretamente pela interface gráfica.
3.Para testar manualmente, utilize o endpoint de conversão de moedas /convert. Exemplo de requisição:

~~~~shell
curl -X 'POST' \
  'http://127.0.0.1:8000/convert' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "from_currency": "USD",
  "to_currency": "EUR",
  "amount": 100
}'
~~~~


Isso retornará a conversão de 100 USD para EUR.

## Passo 7: Alterar as Taxas de Conversão
Se você está utilizando taxas de conversão predefinidas no código, pode ajustá-las manualmente. Abra o arquivo que contém as taxas e altere os valores conforme necessário.

Exemplo:

~~~~shell
conversion_rates = {
    "USD": {"EUR": 0.85, "BRL": 5.25},
    "EUR": {"USD": 1.17, "BRL": 6.18},
    "BRL": {"USD": 0.19, "EUR": 0.16},
}
~~~~


## Passo 8: Finalizar o Ambiente Virtual
Se você usou um ambiente virtual, não se esqueça de desativá-lo após o uso. Para desativar o ambiente virtual, execute:
~~~~shell
deactivate
~~~~
