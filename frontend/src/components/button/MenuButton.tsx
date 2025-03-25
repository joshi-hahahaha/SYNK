import React from "react";
import { motion } from "framer-motion";
import { FaBars } from "react-icons/fa";

type MenuButtonProps = {
  isOpen: boolean;
  setIsOpen: (isOpen: boolean) => void;
};

const MenuButton = ({ isOpen, setIsOpen }: MenuButtonProps) => {
  return (
    <motion.button
      className="w-16 h-16 rounded-full bg-green-500 flex items-center justify-center shadow-lg text-white text-2xl relative z-[1200]"
      onClick={() => setIsOpen(!isOpen)}
      whileTap={{ scale: 0.9 }}
      initial={{ rotate: 0 }}
      animate={{ rotate: isOpen ? 180 : 0 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
    >
      <FaBars />
    </motion.button>
  );
};

export default MenuButton;
