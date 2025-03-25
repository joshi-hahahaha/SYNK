import React from "react";
import { useAuth } from "@/context/AuthContext";

function AuthModal() {
  const { isLogin } = useAuth();

  return (
    <dialog id="auth_modal" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-2xl">{isLogin ? "Login" : "Register"}</h3>
        <p className="py-4">going to put fields here for later</p>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
}

export default AuthModal;
