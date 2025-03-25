import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: false,
  images: {
    domains: ["img.daisyui.com"], // Add your domains here
    // OR use the newer remotePatterns for more control:
    // remotePatterns: [
    //   {
    //     protocol: 'https',
    //     hostname: 'img.daisyui.com',
    //     pathname: '/images/**',
    //   },
    // ],
  },
};

export default nextConfig;
