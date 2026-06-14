import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/upload":    "https://document-intelligence-system-production.up.railway.app",
      "/documents": "https://document-intelligence-system-production.up.railway.app",
      "/ask":       "https://document-intelligence-system-production.up.railway.app",
      "/check-email":"https://document-intelligence-system-production.up.railway.app",
      "/dashboard": "https://document-intelligence-system-production.up.railway.app",
    },
  },
});