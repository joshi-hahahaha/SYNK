"use client";

import React, { createContext, useContext, useState } from "react";

interface AuthContextType {
  isLogin: boolean;
  setIsLogin: (value: boolean) => void;
  openLoginModal: () => void;
  openRegisterModal: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLogin, setIsLogin] = useState(false);

  const openLoginModal = () => {
    setIsLogin(true);
    (
      document.getElementById("auth_modal") as HTMLDialogElement | null
    )?.showModal();
  };

  const openRegisterModal = () => {
    setIsLogin(false);
    (
      document.getElementById("auth_modal") as HTMLDialogElement | null
    )?.showModal();
  };

  return (
    <AuthContext.Provider
      value={{ isLogin, setIsLogin, openLoginModal, openRegisterModal }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
