import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom';

import Header from './components/Header';
import ProductList from './components/ProductList';
import Cart from './components/Cart';

import hobbit from "./assets/books/robbit.jpg";
import harryPotter from "./assets/books/harry_potter.png";
import domCasmurro from "./assets/books/dom_casmurro.jpg";
import pequenoPrincipe from "./assets/books/pequeno_principe.jpg";
import livro1984 from "./assets/books/1984.jpg";
import orgulhoPreconceito from "./assets/books/orgulho_preconceito.jpg";

const products = [
  {
    id: 1,
    name: 'O Hobbit',
    price: 39.90,
    image: hobbit
  },
  {
    id: 2,
    name: 'Harry Potter e a Pedra Filosofal',
    price: 49.90,
    image: harryPotter
  },
  {
    id: 3,
    name: 'Dom Casmurro',
    price: 29.90,
    image: domCasmurro
  },
  {
    id: 4,
    name: 'O Pequeno Príncipe',
    price: 34.90,
    image: pequenoPrincipe
  },
  {
    id: 5,
    name: '1984',
    price: 42.90, 
    image: livro1984
  },
  {
    id: 6,
    name: 'Orgulho e Preconceito',
    price: 44.90,
    image: orgulhoPreconceito
  }
];

const App = () => {
  return (
    <BrowserRouter>

      <Header />

      <Routes>

        <Route
          path="/"
          element={<ProductList products={products} />}
        />

        <Route
          path="/cart"
          element={<Cart />}
        />

      </Routes>

      <footer className="footer">
        <p>
          © 2026 Livraria Online
        </p>

        <span>
          Uma boa história começa com um livro.
        </span>
      </footer>

    </BrowserRouter>
  );
};

export default App;