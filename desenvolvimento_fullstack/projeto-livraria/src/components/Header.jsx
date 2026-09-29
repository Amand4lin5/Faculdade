import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

const Header = () => {
  const cart = useSelector((state) => state.cart);

  return (
    <header className="header">
      <div className="header-content">

        <Link to="/" className="logo">
          <div className="logo-icon">
            📚
          </div>

          <div>
            <h1>Livraria</h1>
            <span>ONLINE</span>
          </div>
        </Link>

        <nav>
          <Link to="/" className="nav-link">
            Início
          </Link>

          <Link to="/cart" className="cart-link">
            <span>🛒</span>
            Carrinho

            {cart.length > 0 && (
              <span className="cart-badge">
                {cart.length}
              </span>
            )}
          </Link>
        </nav>

      </div>
    </header>
  );
};

export default Header;