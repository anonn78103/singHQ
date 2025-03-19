self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('winrate-cache-v1').then(cache => {
            return cache.addAll([
                '/calc/',
                '/calc/index.html',
                '/calc/manifest.json',
                '/calc/icon_TROPHY-modified (1).png'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
