import React, { useEffect, useState } from "react";
import ProductCard from "./ProductCard";
import { useAppContext } from "../MyContext";

function ProductList({ searchTerm, selectedCategory }) {
  const [products, setProducts] = useState([]);

  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  // const baseURL = "https://ecomart-x0ur.onrender.com/products";

  useEffect(() => {
    fetch("http://127.0.0.1:5555/products")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setProducts(data);
        setIsLoading(false);
      })
      .catch((err) => {
        setError(err);
        setIsLoading(false);
      });
  }, []);

  // const handleSearch = (e) => {
  //   setSearchTerm(e.target.value);
  // };
  // console.log(selectedCategory);
  // const filteredProducts = products.filter((product) => {
  //   const matchesSearchTerm = product.prod_name
  //     .toLowerCase()
  //     .includes(searchTerm.toLowerCase());
  //   const matchesCategory =
  //     selectedCategory === "all" || product.category === selectedCategory;
  //   return matchesSearchTerm && matchesCategory;
  // });
  // console.log(products);
  // products.length > 0 ? [...new Set(products.map((item) => item.category))];

  const filteredProducts = products.filter((prod) => {
    if (searchTerm == "") {
      return prod;
    } else if (
      prod.prod_name.toLowerCase().includes(searchTerm.toLowerCase())
    ) {
      return prod;
    }
  });
  // console.log(filteredProducts);
  return (
    <section>
      {/* <SearchFilter
        onSearch={handleSearch}
        onCategoryChange={(e) => setSelectedCategory(e.target.value)}
        query={searchTerm}
        category={selectedCategory}
      /> */}
      <div className="flex flex-wrap flex-1 gap-[2rem] justify-center list-card">
        {filteredProducts.map((product) => {
          return (
            <ProductCard
              key={product.id}
              id={product.id}
              image={product.image}
              price={product.price}
              name={product.prod_name}
              description={product.prod_description}
            />
          );
        })}
      </div>
    </section>
  );
}

export default ProductList;
