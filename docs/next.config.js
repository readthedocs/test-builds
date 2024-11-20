const withMarkdoc = require('@markdoc/next.js');
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',
 
  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  trailingSlash: true,
}

module.exports =
  withMarkdoc({mode: 'static'})({
    pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdoc'],
    ...nextConfig, // Include nextConfig in the export
  });

