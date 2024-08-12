/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        custom: {
          '314455': '#314455',
          '644e5b': '#644e5b',
          '9e5a63': '#9e5a63',
          'c96567': '#c96567',
          '97aabd': '#97aabd',
        }
      }
    },
  },
  plugins: [],
}

