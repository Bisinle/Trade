import React, { useEffect, useState } from "react";
import AOS from "aos";
import "aos/dist/aos.css";

import { AiOutlineHeart } from "react-icons/ai";
import { useAppContext } from "../MyContext";
import { toast } from "react-toastify";

function ProductCard({ id, image, price, name, description }) {
  const {
    setCartCount,
    setWishlistCount,
    cartCount,
    wishlistCount,
    setProducts,
    setQuantity,
  } = useAppContext();

  const addToCart = (prodid) => {
    const found = cartCount.find((element) => element === prodid);

    if (found) {
      toast.info("This item is already in your cart.");
    } else {
      const updatedCart = [...cartCount, prodid];
      setCartCount(updatedCart);
      const product = { id, image, price, name, description };
      setProducts((prevProducts) => [...prevProducts, product]);

      setQuantity((prevQuantity) => [...prevQuantity, 1]);

      localStorage.setItem("cart", JSON.stringify(updatedCart));
    }
  };

  useEffect(() => {
    AOS.init();
  }, []);
  const addToWishlist = (prod) => {
    const found = wishlistCount.find((element) => element.id === prod.id);
    // console.log(prod);

    if (found) {
      toast.info("This item is already on your wishlist.");
    } else {
      const updatedWishlist = [prod, ...wishlistCount];
      setWishlistCount(updatedWishlist);
      localStorage.setItem("wishlist", JSON.stringify(updatedWishlist));
    }
  };

  useEffect(() => {
    const savedWishlist = JSON.parse(localStorage.getItem("wishlist")) || [];
    const savedCart = JSON.parse(localStorage.getItem("cart")) || [];

    setWishlistCount(savedWishlist);
    setCartCount(savedCart);
  }, []);

  return (
    <article
      product={id}
      className="product-card shadow-lg"
      data-aos="fade-up"
      data-aos-duration="500"
      data-aos-once="true"
    >
      <div className="product-image">
        <img
          src={image}
          alt="product-image"
          className="rounded-sm  prod-image"
        />
      </div>
      <div className="product_details card-details">
        <p>{name}</p>
        <p>{price}</p>
      </div>
      <div className="product_card_footer card-details items-center ">
        <button
          onClick={() => addToCart(id)}
          className="bg-transparent border-2 border-black rounded-full px-3 py-2 
        text-md hover:bg-black hover:text-white"
        >
          Add to cart
        </button>
        <AiOutlineHeart
          onClick={() => addToWishlist({ id, image, price, name, description })}
          className="nav-icons"
        />
      </div>
    </article>
  );
}

export default ProductCard;
