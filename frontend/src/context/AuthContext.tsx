"use client";

import React, { createContext, useContext, useState, useEffect } from "react";

interface AuthContextType {
  isLogin: boolean;
  setIsLogin: (value: boolean) => void;
  openLoginModal: () => void;
  openRegisterModal: () => void;
  toggleIsLogin: () => void;
  isAuthenticated: boolean;
  userId: string | null;
  token: string | null;
  login: (token: string, userId: string) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLogin, setIsLogin] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);
  const [token, setToken] = useState<string | null>(null);

  // Initialize auth state from localStorage
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    const storedUserId = localStorage.getItem("userId");
    if (storedToken && storedUserId) {
      setIsAuthenticated(true);
      setToken(storedToken);
      setUserId(storedUserId);
    }
  }, []);

  const login = (newToken: string, newUserId: string) => {
    localStorage.setItem("token", newToken);
    localStorage.setItem("userId", newUserId);
    setIsAuthenticated(true);
    setToken(newToken);
    setUserId(newUserId);
    (
      document.getElementById("auth_modal") as HTMLDialogElement | null
    )?.close();
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("userId");
    setIsAuthenticated(false);
    setToken(null);
    setUserId(null);
    (
      document.getElementById("settings_modal") as HTMLDialogElement | null
    )?.close();
  };

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

  const toggleIsLogin = () => {
    setIsLogin((prev) => !prev);
  };

  return (
    <AuthContext.Provider
      value={{
        isLogin,
        setIsLogin,
        openLoginModal,
        openRegisterModal,
        toggleIsLogin,
        isAuthenticated,
        userId,
        token,
        login,
        logout,
      }}
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
