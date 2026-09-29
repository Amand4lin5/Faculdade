# Livraria Online

Aplicação web de uma livraria online desenvolvida com **React**, **Redux** e **React Router**. O projeto foi desenvolvido com o objetivo de aplicar conceitos de **componentização**, **gerenciamento de estado global** e **navegação entre páginas** em uma aplicação de e-commerce.

## Sobre o projeto

A Livraria Online permite que o usuário visualize uma coleção de livros, adicione produtos ao carrinho de compras, consulte os itens selecionados e remova produtos do carrinho.

O estado do carrinho é gerenciado de forma global utilizando **Redux**, permitindo que diferentes componentes da aplicação compartilhem e atualizem essas informações.

## Funcionalidades

* Visualização dos livros disponíveis
* Adição de livros ao carrinho
* Contador de itens no carrinho
* Visualização dos produtos adicionados
* Remoção de produtos do carrinho
* Cálculo do valor total dos produtos
* Navegação entre página de produtos e carrinho
* Interface responsiva
* Interface com identidade visual em tons de azul

## Tecnologias utilizadas

* **React** — desenvolvimento da interface
* **Vite** — criação e execução do projeto
* **Redux** — gerenciamento do estado global
* **React Redux** — integração do Redux com React
* **React Router DOM** — gerenciamento das rotas
* **JavaScript** — lógica da aplicação
* **CSS** — estilização e responsividade

## 📁 Estrutura do projeto

```text
projeto-livraria/
│
├── public/
│
├── src/
│   ├── components/
│   │   ├── Cart.jsx
│   │   ├── Header.jsx
│   │   └── ProductList.jsx
│   │
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
│   └── store.js
│
├── .gitignore
├── package.json
├── package-lock.json
└── README.md
```

### Componentes principais

#### `ProductList.jsx`

Responsável por apresentar os livros disponíveis e permitir que o usuário adicione um produto ao carrinho.

A ação de adicionar um produto é enviada para o Redux por meio do `dispatch`.

#### `Cart.jsx`

Responsável por apresentar os produtos adicionados ao carrinho.

Utiliza `useSelector` para acessar o estado global do carrinho e `useDispatch` para realizar a remoção dos produtos.

#### `Header.jsx`

Responsável pela navegação da aplicação e pelo acesso à página do carrinho.

Também apresenta a quantidade de produtos adicionados.

#### `store.js`

Responsável pela configuração do Redux e pelo gerenciamento do estado global do carrinho.

O estado possui a seguinte estrutura:

```javascript
{
  cart: []
}
```

As principais ações são:

```text
ADD_TO_CART
REMOVE_FROM_CART
```

#### `App.jsx`

Responsável pela estrutura principal da aplicação e pela configuração das rotas.

As principais rotas são:

```text
/       → Lista de produtos
/cart   → Carrinho de compras
```

## Funcionamento do carrinho

O fluxo de adição de um produto funciona da seguinte maneira:

```text
Usuário
   │
   ▼
Clica em "Adicionar"
   │
   ▼
ProductList
   │
   ▼
dispatch(ADD_TO_CART)
   │
   ▼
Redux Store
   │
   ▼
cartReducer
   │
   ▼
Estado do carrinho atualizado
   │
   ▼
Cart
```

Para remover um produto:

```text
Usuário
   │
   ▼
Clica em "Remover"
   │
   ▼
Cart
   │
   ▼
dispatch(REMOVE_FROM_CART)
   │
   ▼
Redux Store
   │
   ▼
cartReducer
   │
   ▼
Produto removido
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/projeto-livraria-online.git
```

### 2. Entrar no diretório

```bash
cd projeto-livraria-online
```

### 3. Instalar as dependências

```bash
npm install
```

### 4. Executar o projeto

```bash
npm run dev
```

Após executar o comando, o Vite disponibilizará a aplicação localmente, normalmente em:

```text
http://localhost:5173
```

