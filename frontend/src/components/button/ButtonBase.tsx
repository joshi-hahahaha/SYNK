import React, { JSX } from "react";
import { motion } from "framer-motion";

type ButtonBaseProps = {
  index: number;
  btn: Btn;
};

type Btn = {
  icon: JSX.Element;
  color: string;
  angle: number;
  type: string;
};

const ButtonBase = ({ index, btn }: ButtonBaseProps) => {
  const handleClick = () => {
    console.log(btn.type);
  };

  return (
    <motion.button
      key={index}
      className={`absolute bottom-2 w-16 h-16 rounded-full flex items-center justify-center text-white text-lg shadow-lg glass ${btn.color} z-[1100] hover:cursor-pointer`}
      initial={{ opacity: 0, scale: 0 }}
      animate={{
        opacity: 1,
        scale: 1,
        x: 80 * Math.cos((btn.angle * Math.PI) / 180),
        y: 80 * Math.sin((btn.angle * Math.PI) / 180),
      }}
      exit={{ opacity: 0, scale: 0 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      onClick={handleClick}
    >
      {btn.icon}
    </motion.button>
  );
};

export default ButtonBase;
