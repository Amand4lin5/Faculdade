import { useDispatch } from 'react-redux';

const ProductList = ({ products }) => {
  const dispatch = useDispatch();

  const addToCart = (product) => {
    dispatch({
      type: 'ADD_TO_CART',
      payload: product
    });
  };

  return (
    <main className="products-page">
      <section className="hero">
        <div>
          <p className="hero-label">BEM-VINDO À LIVRARIA</p>

          <h2>
            Encontre sua próxima
            <span> grande leitura.</span>
          </h2>

          <p>
            Explore nossa seleção de livros e adicione
            seus favoritos ao carrinho.
          </p>
        </div>
      </section>

      <section className="books-section">
        <div className="section-header">
          <div>
            <p className="section-label">NOSSA COLEÇÃO</p>
            <h2>Livros disponíveis</h2>
          </div>

          <span className="book-count">
            {products.length} livros
          </span>
        </div>

        <div className="books-grid">
          {products.map((product) => (
            <div className="book-card" key={product.id}>
              
              <div className="book-image-container">
                <img
                  src={product.image}
                  alt={`Capa do livro ${product.name}`}
                  className="book-image"
                />
              </div>

              <div className="book-content">
                <span className="book-category">LIVRO</span>

                <h3>{product.name}</h3>

                <p className="book-description">
                  Uma excelente escolha para sua próxima leitura.
                </p>

                <div className="book-footer">
                  <strong>
                    R$ {product.price.toFixed(2).replace('.', ',')}
                  </strong>

                  <button
                    onClick={() => addToCart(product)}
                    className="add-button"
                  >
                    + Adicionar
                  </button>
                </div>
              </div>

            </div>
          ))}
        </div>
      </section>
    </main>
  );
};

export default ProductList;