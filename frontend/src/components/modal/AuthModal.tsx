import React, { useState } from "react";
import { useAuth } from "@/context/AuthContext";
import { AuthData } from "@/type";

function AuthModal() {
  const { isLogin, toggleIsLogin } = useAuth();

  const [data, setData] = useState<AuthData>({
    email: "",
    password: "",
    username: "",
    confirmPassword: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Form submitted:", data);
    // Add your authentication logic here
  };

  return (
    <dialog id="auth_modal" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-2xl mb-6">
          {isLogin ? "Login" : "Register"}
        </h3>

        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Username (only shown for register) */}
          {!isLogin && (
            <div className="form-control">
              <label className="label">
                <span className="label-text">Username</span>
              </label>
              <input
                type="text"
                name="username"
                placeholder="Enter your username"
                className="input input-bordered w-full"
                value={data.username}
                onChange={handleChange}
                required={!isLogin}
              />
            </div>
          )}

          {/* Email */}
          <div className="form-control">
            <label className="label">
              <span className="label-text">Email</span>
            </label>
            <input
              type="email"
              name="email"
              placeholder="Enter your email"
              className="input input-bordered w-full"
              value={data.email}
              onChange={handleChange}
              required
            />
          </div>

          {/* Password */}
          <div className="form-control">
            <label className="label">
              <span className="label-text">Password</span>
            </label>
            <input
              type="password"
              name="password"
              placeholder="Enter your password"
              className="input input-bordered w-full"
              value={data.password}
              onChange={handleChange}
              required
            />
          </div>

          {/* Confirm Password (only shown for register) */}
          {!isLogin && (
            <div className="form-control">
              <label className="label">
                <span className="label-text">Confirm Password</span>
              </label>
              <input
                type="password"
                name="confirmPassword"
                placeholder="Confirm your password"
                className="input input-bordered w-full"
                value={data.confirmPassword}
                onChange={handleChange}
                required={!isLogin}
              />
            </div>
          )}
          <p className="py-1">
            {isLogin ? (
              <>
                Need an account?{" "}
                <span
                  className="text-blue-500 cursor-pointer"
                  onClick={toggleIsLogin}
                >
                  Register here!
                </span>
              </>
            ) : (
              <>
                Already have an account?{" "}
                <span
                  className="text-blue-500 cursor-pointer"
                  onClick={toggleIsLogin}
                >
                  Login here!
                </span>
              </>
            )}
          </p>

          <div className="modal-action">
            <button type="submit" className="btn btn-primary">
              {isLogin ? "Login" : "Register"}
            </button>
            <button
              type="button"
              onClick={() =>
                (
                  document.getElementById("auth_modal") as HTMLDialogElement
                )?.close()
              }
              className="btn"
            >
              Close
            </button>
          </div>
        </form>
      </div>

      {/* Modal backdrop close */}
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
}

export default AuthModal;
