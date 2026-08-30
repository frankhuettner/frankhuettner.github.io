// @ts-check
import { defineConfig, fontProviders } from "astro/config";
import { unified } from "@astrojs/markdown-remark";
import sitemap from "@astrojs/sitemap";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

export default defineConfig({
  site: "https://huettner.io",

  integrations: [sitemap()],

  markdown: {
    // Sätteri (Astro 7's default) has no math support, so use the unified
    // pipeline for KaTeX. Math renders at build time — no runtime MathJax.
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeKatex],
    }),
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark" },
    },
  },

  // Self-hosted at build time: no CDN, no third-party request at runtime.
  fonts: [
    {
      provider: fontProviders.google(),
      name: "Source Serif 4",
      cssVariable: "--font-serif",
      weights: [400, 600, 700],
      styles: ["normal", "italic"],
      subsets: ["latin", "latin-ext"],
      fallbacks: ["Charter", "Georgia", "serif"],
    },
    {
      provider: fontProviders.google(),
      name: "IBM Plex Mono",
      cssVariable: "--font-mono",
      weights: [400, 500],
      subsets: ["latin", "latin-ext"],
      fallbacks: ["ui-monospace", "SFMono-Regular", "monospace"],
    },
  ],
});
