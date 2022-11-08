import React from "react";

function login() {
  return (
    <div className="bg-[url('/signin.png')] bg-cover bg-no-repeat">
      <div className=" min-h-screen flex flex-col text-white">
        <div className="container max-w-lg mx-auto flex-1 flex flex-col items-center justify-center px-2">
          <div className="backdrop-blur-3xl shadow-2xl px-12 py-12 rounded  text-black w-full">
            <h1 className="mb-8 text-5xl text-center text-white font-bold">Log In</h1>

            <input
              type="text"
              className="block bg-black bg-opacity-0 border border-grey-light w-full p-3 rounded mb-4"
              name="email"
              placeholder="Email"
              required
            />

            <input
              type="password"
              className="block bg-black bg-opacity-0 border border-grey-light w-full p-3 rounded mb-4"
              name="password"
              placeholder="Password"
              required
            />
            <button
              type="submit"
              className="w-full text-center py-3 rounded bg-medium-slate-blue bg-opacity-10 opacity-10 hover:opacity-100 hover:shadow-lg delay-4000 text-white hover:bg-green-dark focus:outline-none my-1"
            >
              Login
            </button>

          </div>
          <div className="text-grey-dark mt-6">
            Dont have an acount?
            <a
              className="no-underline border-b border-blue text-blue"
              href="/signup"
            >
              Sign up
            </a>
            .
          </div>
        </div>
      </div>
    </div>
  );
}

export default login;
