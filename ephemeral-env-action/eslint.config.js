const tsParser = require("@typescript-eslint/parser");
const tsPlugin = require("@typescript-eslint/eslint-plugin");
const googleConfig = require("eslint-config-google");
const globals = require("globals");

module.exports = [
  {
    ignores: ["dist/**", "lib/**", "node_modules/**"]
  },

  // Google config patched for ESLint v9+
  {
    ...googleConfig,
    rules: {
      ...googleConfig.rules,

      // Removed ESLint core rules (must disable)
      "valid-jsdoc": "off",
      "require-jsdoc": "off"
    }
  },

  // TypeScript override
  {
    files: ["**/*.ts"],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 2018,
        sourceType: "module"
      },
      globals: {
        ...globals.node,
        Atomics: "readonly",
        SharedArrayBuffer: "readonly"
      }
    },
    plugins: {
      "@typescript-eslint": tsPlugin
    },
    rules: {
      "max-len": "off"
    }
  }
];
