"use client";

import { motion, AnimatePresence } from "framer-motion";
import { useState } from "react";
import { FaBars, FaTrash, FaPencilAlt, FaInfoCircle } from "react-icons/fa";

export default function ButtonMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    { icon: <FaPencilAlt />, color: "bg-yellow-400", angle: 180 },
    { icon: <FaInfoCircle />, color: "bg-blue-500", angle: -60 },
    { icon: <FaTrash />, color: "bg-red-400", angle: -120 },
    { icon: <FaTrash />, color: "bg-red-400", angle: 0 },
  ];

  return (
    <div className="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-[1000]">
      {/* Main Button */}
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

      {/* Floating Items */}
      <AnimatePresence>
        {isOpen &&
          menuItems.map((item, index) => (
            <motion.button
              key={index}
              className={`absolute bottom-2 w-16 h-16 rounded-full flex items-center justify-center text-white text-lg shadow-lg ${item.color} z-[1100]`} // Ensure buttons stay above the map
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
          ))}
      </AnimatePresence>
    </div>
  );
}
