/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    
    extend: {
      colors: {
        "light-yellow": "#fffbd8ff",
        "medium-slate-blue": "#7a59ffff",
        "duke-blue": "#0800a0ff",
        "black-chocolate": "#6",
        "rose-red": "#cc005cff",
      },
      backgroundImage: {
        'cool-space': "url('./public/coolspace.jpg)",
      },
      fontFamily: {
        attures: ["Atures"],
        space: ["Space Legion"],
        grotesk: ['Space Grotesk']
      },
    },
  },
  plugins: [],
}
