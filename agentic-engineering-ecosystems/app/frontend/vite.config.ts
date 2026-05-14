import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 9091,
    allowedHosts: true,
    proxy: {
      '/auth': 'http://localhost:9090',
      '/api': 'http://localhost:9090',
    },
  },
})
