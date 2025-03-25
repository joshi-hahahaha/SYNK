"use client";

import { AnimatePresence } from "framer-motion";
import { useState } from "react";
import { FaCalendar, FaSearch, FaSpinner, FaCog } from "react-icons/fa";
import MenuButton from "./MenuButton";
import ButtonBase from "./ButtonBase";

export default function ButtonMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    {
      icon: <FaCalendar />,
      color: "bg-yellow-400",
      angle: 180,
      type: "Events",
    },
    { icon: <FaSearch />, color: "bg-teal-400", angle: -120, type: "search" },
    {
      icon: <FaSpinner />,
      color: "bg-green-400",
      angle: -60,
      type: "Refresh",
    },
    { icon: <FaCog />, color: "bg-blue-400", angle: 0, type: "Settings" },
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
