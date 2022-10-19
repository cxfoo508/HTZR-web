// next.config.js
const withImages = require('next-images');

/** @type {import('next').NextConfig} */
module.exports = withImages({
  eslint: {
    dirs: ['src'],
  },

  reactStrictMode: true,

  exportPathMap: async function () {
    return {
      '/': { page: '/' },
    };
  },

  images: {
    loader: 'akamai',
    path: '',
  },

  publicRuntimeConfig: {
    devUrl: "http://localhost:5000",
  },
  // Uncoment to add domain whitelist
  // images: {
  //   domains: [
  //     'res.cloudinary.com',
  //   ],
  // },

  // SVGR
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/i,
      issuer: /\.[jt]sx?$/,
      use: [
        {
          loader: '@svgr/webpack',
          options: {
            typescript: true,
            icon: true,
          },
        },
      ],
    });

    return config;
  },
});
