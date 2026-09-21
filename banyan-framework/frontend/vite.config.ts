import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: { outDir: '../control-plane-go/internal/webassets/dist', emptyOutDir: true },
});
