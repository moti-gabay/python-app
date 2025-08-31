
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  baseHref: '/',
  locale: undefined,
  routes: [
  {
    "renderMode": 2,
    "redirectTo": "/login",
    "route": "/"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-JFEEC4SH.js"
    ],
    "route": "/login"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-3BSI734K.js"
    ],
    "route": "/files"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-7WGLK5HH.js"
    ],
    "route": "/homepage"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-7FI62R6Y.js",
      "chunk-QTKABZHD.js"
    ],
    "route": "/images"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-TXCRSLPS.js",
      "chunk-QTKABZHD.js",
      "chunk-BC6JWCRN.js",
      "chunk-Q4HXHNX7.js"
    ],
    "route": "/dashboard"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-VKX6T6LQ.js",
      "chunk-VTWTRM6P.js"
    ],
    "route": "/news"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-S4RPOCWL.js",
      "chunk-VTWTRM6P.js"
    ],
    "route": "/news/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-EKB74VFV.js",
      "chunk-VTWTRM6P.js"
    ],
    "route": "/edit-news/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-PIUBCAFZ.js",
      "chunk-VTWTRM6P.js"
    ],
    "route": "/add-news"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-7YJHL3AA.js",
      "chunk-IZI5MAW3.js"
    ],
    "route": "/tradition"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-G4N2FZHH.js",
      "chunk-IZI5MAW3.js"
    ],
    "route": "/tradition/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-DQ7VG4UE.js",
      "chunk-IZI5MAW3.js"
    ],
    "route": "/edit-tradition/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-ZZ6FYHWD.js",
      "chunk-IZI5MAW3.js"
    ],
    "route": "/add-tradition"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-D4YCW4DS.js",
      "chunk-Q4HXHNX7.js"
    ],
    "route": "/events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-MB3I4PNL.js",
      "chunk-BC6JWCRN.js",
      "chunk-Q4HXHNX7.js"
    ],
    "route": "/admin-events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-X5J74NZS.js"
    ],
    "route": "/contact"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-IIRHQIHE.js",
      "chunk-Q4HXHNX7.js"
    ],
    "route": "/add-event"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EUU6O7ZX.js"
    ],
    "route": "/donation"
  },
  {
    "renderMode": 2,
    "redirectTo": "/login",
    "route": "/**"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 29299, hash: '805413039deaa3f4b914946f9a8b5ecb4469ab8490a5dff074090fb7f619eb2f', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '44d0531b37888ffb0d05074cb073aa27647f4e9cde53acb82032eb2f53b19479', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: 'e1b16bc6201bbc81cb1fc6f24e683cd02b566fbb7feb4c7b3bbf2908d7426237', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: 'b89db33c5164a140a42a41ed9b9b7a74a574a0cb18165b56b505d0023ff280d4', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '40e88aebea002416df2fa04032e672fc3c7424d940f30f645f63a81438634eef', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '83466ae068e627bd8e5ca4dd63f7497febfe3f4f17211f8a197705a34e250b55', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '8862b7aba94534c91b0b2dd54753201b16becd4697e040503fd1b29d8f4fb7f8', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '760a58b4c44ffb05775fcdd8ea38caabc312e62e3e2a5068e52b2196a48e783d', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: 'a739460fae6cb69fad6d5a683de107f6fcf98e3627f61a7e96d1eadd55f831e9', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: '1db7e272266a8e4d8a23f325dbda9348fc52ebc34b1ffde77983e213e54f34cc', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '5a900b48a43f1f08a4f8b0e34574edd0b73f896835a72cd28e00629e82f57081', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: 'de69f6c22a71e2cb98b2f403584cf5f21a2d6291cf832920f8db9f8a78835bc7', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: '9af2efa77d25c440de5b63cd7bd146e9283d6e9f7c4cd98d78182d523c70493e', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: 'f7ba4b50bc7225e2932991826fc14c038b3ff655b7ab666b934c8bd9223eff1b', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: 'ff3893ef2da9cdd1bc7d95e4dd6fb559f8b541e7c9a3c1feb0848dca98483345', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: 'cf49fe38c6d7f6bee06346409a852071306f36f0f0220e7f9be238cd2420aa64', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-FOAOTY4F.css': {size: 329941, hash: 'Mi+gaaif+vg', text: () => import('./assets-chunks/styles-FOAOTY4F_css.mjs').then(m => m.default)}
  },
};
