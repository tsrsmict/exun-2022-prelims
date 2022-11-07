/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors: {
      "cream-yellow": "#f3ffbdff",
      "blue-sapphire": "#086375ff",
      "dark-turquoise": "#25ced1ff",
      "dark-purple": "#23001eff",
      "magenta-pink": "#d30c7bff"
    },
    extend: {},
  },
  plugins: [],
}
