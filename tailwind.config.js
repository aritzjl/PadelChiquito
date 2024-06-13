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
        'gray-fog': '#F1F5F9',
      },
      screens: {
        'xs': '425px',
      },
    },
  },
  plugins: [
    function ({ addUtilities }) {
      const newUtilities = {
        '.scrollbar-hidden': {
          scrollbarWidth: 'none',
          msOverflowStyle: 'none',
          '&::-webkit-scrollbar': {
            display: 'none',
          },
        },
      };
      addUtilities(newUtilities, ['responsive', 'hover']);
    },
  ],
}