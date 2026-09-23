import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    // Backend runs on localhost in dev; safe to allow here since this is
    // our own API, not arbitrary user-supplied URLs.
    dangerouslyAllowLocalIP: true,
    remotePatterns: [
      {
        protocol: "http",
        hostname: "localhost",
        port: "8000",
        pathname: "/static/**",
      },
      {
        protocol: "http",
        hostname: "localhost",
        port: "8000",
        pathname: "/media/**",
      },
    ],
  },
};

export default nextConfig;
