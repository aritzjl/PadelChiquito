/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'electric-lime': '#ccff00',
        'lime-zest': '#d9ff00',
      },
      screens: {
        'xs': '425px',
      },
    },
  },
  plugins: [],
}