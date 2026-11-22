/**
 * AWDEV Cloudflare Worker (awdev.eu.org)
 * Serves static assets from env.ASSETS with clean URLs, custom 404 fallback,
 * security headers, and cache control.
 */
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Block unwanted methods early
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method Not Allowed", {
        status: 405,
        headers: { Allow: "GET, HEAD" },
      });
    }

    try {
      // 1. Try serving exact or asset-matched file from env.ASSETS
      let response = await env.ASSETS.fetch(request);

      // 2. If not found and path has no file extension, try "<path>.html"
      if (response.status === 404 && !url.pathname.includes(".")) {
        const cleanPath = url.pathname.endsWith("/")
          ? `${url.pathname}index.html`
          : `${url.pathname}.html`;

        const htmlRequest = new Request(new URL(cleanPath, url.origin), request);
        const htmlCandidate = await env.ASSETS.fetch(htmlRequest);
        if (htmlCandidate.ok) {
          response = htmlCandidate;
        }
      }

      // 3. Fallback to custom 404.html if still 404
      if (response.status === 404) {
        const notFoundReq = new Request(new URL("/404.html", url.origin), request);
        const custom404 = await env.ASSETS.fetch(notFoundReq);
        if (custom404.ok) {
          response = new Response(custom404.body, {
            status: 404,
            statusText: "Not Found",
            headers: custom404.headers,
          });
        }
      }

      // Clone headers so we can safely attach SEO, caching & security headers
      const headers = new Headers(response.headers);
      headers.set("X-Content-Type-Options", "nosniff");
      headers.set("X-Frame-Options", "SAMEORIGIN");
      headers.set("Referrer-Policy", "strict-origin-when-cross-origin");

      // Cache policy: immutable-ish for static assets, short/revalidate for HTML
      if (/\.(css|js|jpg|jpeg|png|webp|svg|ico|woff2?)$/i.test(url.pathname)) {
        headers.set("Cache-Control", "public, max-age=86400, stale-while-revalidate=604800");
      } else if (response.headers.get("content-type")?.includes("text/html")) {
        headers.set("Cache-Control", "public, max-age=300, must-revalidate");
      }

      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers,
      });
    } catch (err) {
      return new Response(`AWDEV Worker Error: ${err.message}`, {
        status: 500,
        headers: { "Content-Type": "text/plain; charset=utf-8" },
      });
    }
  },
};
