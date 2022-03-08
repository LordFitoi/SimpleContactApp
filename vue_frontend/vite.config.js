const { resolve } = require('path');
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const staticPath = '../zero_note/static/vue/';
const appsEntries = {
    overview: resolve('./src/main.js')
}

export default defineConfig({
    root: resolve(staticPath),
    base: '/static/',
    plugins: [vue()],
    build: {
        outDir: resolve(staticPath),
        manifest: true,
        emptyOutDir: true,
        rollupOptions: {
            output: {
                entryFileNames: `[name].js`,
                chunkFileNames: `[name].js`,
                assetFileNames: `[name].[ext]`
            },
            input: appsEntries
        },
    }
})