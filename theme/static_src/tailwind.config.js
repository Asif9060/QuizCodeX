/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Django templates
    "../../templates/**/*.html",
    "../../apps/**/templates/**/*.html",
    // JavaScript files with class names
    "../../static/js/**/*.js",
  ],
  darkMode: ["class", '[data-theme="quiz-dark"]'],
  theme: {
    extend: {
      colors: {
        // Quiz Platform design tokens
        surface: {
          DEFAULT: "#0f1117",   // app background
          raised: "#1a1d27",    // card background
          hover: "#242736",     // hover / elevated
          border: "#2e3148",    // border color
        },
        accent: {
          violet: "#7c6df0",
          cyan: "#22d3c8",
          pink: "#f472b6",
        },
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ["JetBrains Mono", "Fira Code", "ui-monospace", "monospace"],
      },
      animation: {
        "fade-in": "fadeIn 0.3s ease-in-out",
        "slide-up": "slideUp 0.3s ease-out",
        "slide-right": "slideRight 0.25s ease-out",
        "score-fill": "scoreFill 1.2s ease-out forwards",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        slideUp: {
          "0%": { opacity: "0", transform: "translateY(16px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        slideRight: {
          "0%": { opacity: "0", transform: "translateX(-16px)" },
          "100%": { opacity: "1", transform: "translateX(0)" },
        },
        scoreFill: {
          "0%": { "--score-pct": "0%" },
          "100%": { "--score-pct": "var(--score-target)" },
        },
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        "quiz-dark": {
          // Primary violet accent
          "primary": "#7c6df0",
          "primary-content": "#ffffff",
          // Secondary cyan accent
          "secondary": "#22d3c8",
          "secondary-content": "#0f1117",
          // Accent pink
          "accent": "#f472b6",
          "accent-content": "#ffffff",
          // Neutral
          "neutral": "#1a1d27",
          "neutral-content": "#e2e8f0",
          // Base colors (surface layers)
          "base-100": "#0f1117",
          "base-200": "#1a1d27",
          "base-300": "#242736",
          "base-content": "#e2e8f0",
          // Semantic colors
          "info": "#3b82f6",
          "success": "#22c55e",
          "warning": "#f59e0b",
          "error": "#ef4444",
          // Border radius
          "--rounded-box": "0.75rem",
          "--rounded-btn": "0.5rem",
          "--rounded-badge": "1.9rem",
          "--tab-radius": "0.5rem",
        },
      },
    ],
    darkTheme: "quiz-dark",
    base: true,
    styled: true,
    utils: true,
    logs: false,
  },
};
