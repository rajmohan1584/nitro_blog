import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/posts': 'http://localhost:8000',
      '/home_json': 'http://localhost:8000',
    },
  },
})
