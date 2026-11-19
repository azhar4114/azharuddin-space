import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://azharuddin.space',
  integrations: [
    tailwind({ applyBaseStyles: false }),
    mdx(),
    // sitemap() — disabled due to @astrojs/sitemap bug with this Astro version; re-enable after upgrade
  ],
  markdown: {
    shikiConfig: {
      theme: 'github-dark-dimmed',
      wrap: true,
    },
  },
});
