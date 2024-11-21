const withMarkdoc = require('@markdoc/next.js');
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',
 
  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  trailingSlash: true,

  // Ensure links are relative
  basePath: process.env.READTHEDOCS_CANONICAL_URL ? new URL(process.env.READTHEDOCS_CANONICAL_URL).pathname : '',
}

module.exports =
  withMarkdoc({mode: 'static'})({
    pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdoc'],
    ...nextConfig, // Include nextConfig in the export
  });

