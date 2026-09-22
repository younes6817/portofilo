/** @type {import('tailwindcss').Config} */
module.exports = {
  // Same engine/version as the old runtime CDN (static/js/tailwind.js = Tailwind 3.4.17),
  // so the generated utilities are identical to what the browser used to build on the fly.
  content: [
    './templates/**/*.html',
    './home/templates/**/*.html',
    './projects/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
