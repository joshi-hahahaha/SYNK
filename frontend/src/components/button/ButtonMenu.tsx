"use client";

import { AnimatePresence } from "framer-motion";
import { useState } from "react";
import { FaTrash, FaPencilAlt, FaInfoCircle } from "react-icons/fa";
import MenuButton from "./MenuButton";
import ButtonBase from "./ButtonBase";

export default function ButtonMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    {
      icon: <FaPencilAlt />,
      color: "bg-yellow-400",
      angle: 180,
      type: "Events",
    },
    {
      icon: <FaInfoCircle />,
      color: "bg-blue-500",
      angle: -60,
      type: "Refresh",
    },
    { icon: <FaTrash />, color: "bg-red-400", angle: -120, type: "search" },
    { icon: <FaTrash />, color: "bg-red-400", angle: 0, type: "Settings" },
  ];

  return (
    <div className="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-[1000]">
      {/* Main Button */}
      <MenuButton isOpen={isOpen} setIsOpen={setIsOpen} />

      {/* Floating Items */}
      <AnimatePresence>
        {isOpen &&
          menuItems.map((btn, index) => (
            <ButtonBase key={index} btn={btn} index={index} />
          ))}
      </AnimatePresence>
    </div>
  );
}
