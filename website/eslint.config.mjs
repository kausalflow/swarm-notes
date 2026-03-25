import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintPluginAstro from 'eslint-plugin-astro';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  ...eslintPluginAstro.configs.recommended,
  {
    ignores: ['dist/**', 'node_modules/**', '.astro/**'],
  },
  {
    rules: {
      // Allow unused vars starting with underscore
      '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
      // Allow any types in some cases (starter kit flexibility)
      '@typescript-eslint/no-explicit-any': 'warn',
    },
  }
);
