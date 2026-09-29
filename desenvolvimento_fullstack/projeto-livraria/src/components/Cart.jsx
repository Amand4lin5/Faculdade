import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';

const Cart = () => {
  const cart = useSelector((state) => state.cart);
  const dispatch = useDispatch();

  const removeFromCart = (product) => {
    dispatch({
      type: 'REMOVE_FROM_CART',
      payload: product
    });
  };

  const total = cart.reduce(
    (sum, item) => sum + item.price,
    0
  );

  return (
    <main className="cart-page">

      <div className="cart-header">
        <div>
          <p className="section-label">SEU PEDIDO</p>
          <h2>Meu Carrinho</h2>
        </div>

        <span className="cart-items-count">
          {cart.length} {cart.length === 1 ? 'item' : 'itens'}
        </span>
      </div>

      {cart.length === 0 ? (
        <div className="empty-cart">

          <div className="empty-cart-icon">
            🛒
          </div>

          <h3>Seu carrinho está vazio</h3>

          <p>
            Adicione alguns livros para começar sua compra.
          </p>

          <Link to="/" className="continue-button">
            Explorar livros
          </Link>

        </div>
      ) : (
        <div className="cart-container">

          <div className="cart-products">

            {cart.map((item, index) => (
              <div
                className="cart-item"
                key={`${item.id}-${index}`}
              >

                <div className="cart-book-icon">
                  📖
                </div>

                <div className="cart-book-info">
                  <h3>{item.name}</h3>

                  <span>
                    R$ {item.price.toFixed(2).replace('.', ',')}
                  </span>
                </div>

                <button
                  className="remove-button"
                  onClick={() => removeFromCart(item)}
                >
                  Remover
                </button>

              </div>
            ))}

          </div>

          <aside className="summary">

            <h3>Resumo do pedido</h3>

            <div className="summary-line">
              <span>Itens</span>
              <span>{cart.length}</span>
            </div>

            <div className="summary-line total-line">
              <span>Total</span>

              <strong>
                R$ {total.toFixed(2).replace('.', ',')}
              </strong>
            </div>

            <button className="checkout-button">
              Finalizar compra
            </button>

            <Link
              to="/"
              className="continue-shopping"
            >
              ← Continuar comprando
            </Link>

          </aside>

        </div>
      )}

    </main>
  );
};

export default Cart;