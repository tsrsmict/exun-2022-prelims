/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors: {
      "light-yellow": "#fffbd8ff",
      "medium-slate-blue": "#7a59ffff",
      "duke-blue": "#0800a0ff",
      "black-chocolate": "#211103ff",
      "rose-red": "#cc005cff"

    },
    extend: {},
  },
  plugins: [],
}
