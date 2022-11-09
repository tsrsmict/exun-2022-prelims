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
        "slate-blue": "#99DDFF",
        "purplish": "#181867",
        "purplish-two": "#4E1867",
        "purplish-three": "#602040",
        "purplish-four": '#661A33',
        "purplish-five": '#750D0D',
        "cute-pink": "#FF99BB",
        "rose-red": "#cc005cff",
        "gray-cool": '#6B6B6B'
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
