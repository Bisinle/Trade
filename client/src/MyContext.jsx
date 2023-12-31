import { createContext, useContext, useState, useEffect } from "react";
import { toast } from "react-toastify";

export const about = ["Home", "About Us", "Sign In", "Contact Us"];

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [cartCount, setCartCount] = useState([]);
  const [wishlistCount, setWishlistCount] = useState([]);
  const [products, setProducts] = useState([]);
  const [quantity, setQuantity] = useState([]);
  const [isLogedin, setIsLogedin] = useState(false);
  const [jwToken, setJwtToken] = useState("");
  const [userRole, setUserRole] = useState("");
  const [userId, setUserId] = useState(null);

  // get token from the localstorage
  // useEffect(() => {
  //   const token = localStorage.getItem("token");

  // }, []);

  // remove item from the wishlist
  const removeFromWishlist = (prod) => {
    const updatedWishlist = wishlistCount.filter(
      (element) => element.id !== prod.id
    );
    setWishlistCount(updatedWishlist);
    localStorage.setItem("wishlist", JSON.stringify(updatedWishlist));
  };

  // add item to cart
  const addToCartFromWishlist = (prod) => {
    const found = cartCount.find((element) => element === prod.id);

    if (found) {
      toast.info("This item is already in your cart.");
    } else {
      const updatedCart = [...cartCount, prod.id];
      setCartCount(updatedCart);

      setProducts((prevProducts) => [...prevProducts, prod]);
      setQuantity((prevQuantity) => [...prevQuantity, 1]);

      localStorage.setItem("cart", JSON.stringify(updatedCart));
    }
  };

  useEffect(() => {
    const role = localStorage.getItem("user_role");
    setUserRole(role);
  }, []);

  return (
    <AppContext.Provider
      value={{
        cartCount,
        setCartCount,
        isLogedin,
        setIsLogedin,
        wishlistCount,
        setWishlistCount,
        products,
        setProducts,
        quantity,
        setQuantity,
        removeFromWishlist,
        addToCartFromWishlist,
        jwToken,
        setJwtToken,
        userRole,
        setUserRole,
        userId,
        setUserId,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  return useContext(AppContext);
};
