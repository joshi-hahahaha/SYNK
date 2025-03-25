import React from "react";
import { motion } from "framer-motion";

function SearchButton() {
  return (
    <motion.button
      className={`absolute w-16 h-16 rounded-full flex items-center justify-center text-white text-lg shadow-lg ${item.color} z-[1100]`} // Ensure buttons stay above the map
      initial={{ opacity: 0, scale: 0 }}
      animate={{
        opacity: 1,
        scale: 1,
        x: 80 * Math.cos((item.angle * Math.PI) / 180),
        y: 80 * Math.sin((item.angle * Math.PI) / 180),
      }}
      exit={{ opacity: 0, scale: 0 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
    >
      {item.icon}
    </motion.button>
  );
}

export default SearchButton;
