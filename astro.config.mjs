// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	// Use the Read the Docs canonical URL so links and assets
	// resolve under the version path (e.g. `/en/starlight/`)
	site: process.env.READTHEDOCS_CANONICAL_URL,
	base: process.env.READTHEDOCS_CANONICAL_URL
		? new URL(process.env.READTHEDOCS_CANONICAL_URL).pathname
		: '/',
	integrations: [
		starlight({
			title: 'Starlight',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/readthedocs/test-builds' }],
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Reference',
					items: [{ autogenerate: { directory: 'reference' } }],
				},
			],
		}),
	],
});
