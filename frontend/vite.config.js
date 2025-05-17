import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: './',  // مهم جداً لو المشروع يُنشر في مجلد فرعي أو بدون دومين فرعي
  plugins: [react()],
});

