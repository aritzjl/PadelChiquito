/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}", "./apps/users/templates/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'electric-lime': '#ccff00',
        'lime-zest': '#d9ff00',
        'vegan-mastermind': '#20cf46',
        'acid-pops': '#41ea67',
      },
      screens: {
        'xs': '425px',
      },
    },
  },
  plugins: [],
}