
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
      "chunk-RDXHCF4S.js"
    ],
    "route": "/login"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-TKMKGGHW.js"
    ],
    "route": "/files"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-5CC6OAKP.js"
    ],
    "route": "/homepage"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-YGQIDCYR.js",
      "chunk-AP6STCCU.js"
    ],
    "route": "/images"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-L67DKT4Y.js",
      "chunk-AP6STCCU.js",
      "chunk-O4TDMWM5.js",
      "chunk-K5IZWYLI.js"
    ],
    "route": "/dashboard"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-IUHORK4M.js",
      "chunk-42XEETT4.js"
    ],
    "route": "/news"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-LXHW2TMT.js",
      "chunk-42XEETT4.js"
    ],
    "route": "/news/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-QAHYZEBE.js",
      "chunk-42XEETT4.js"
    ],
    "route": "/edit-news/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-YAY5QJQU.js",
      "chunk-42XEETT4.js"
    ],
    "route": "/add-news"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-K4WWWCAD.js",
      "chunk-IQMK6W4N.js"
    ],
    "route": "/tradition"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-TMVGZDEN.js",
      "chunk-IQMK6W4N.js"
    ],
    "route": "/tradition/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-YXHNFYJG.js",
      "chunk-IQMK6W4N.js"
    ],
    "route": "/edit-tradition/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EVMA4ZGN.js",
      "chunk-IQMK6W4N.js"
    ],
    "route": "/add-tradition"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-3Z6Q64ZM.js",
      "chunk-K5IZWYLI.js"
    ],
    "route": "/events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-SBAWTNKB.js",
      "chunk-O4TDMWM5.js",
      "chunk-K5IZWYLI.js"
    ],
    "route": "/admin-events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-QLJAAGNN.js"
    ],
    "route": "/contact"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-7QRQMFCU.js",
      "chunk-K5IZWYLI.js"
    ],
    "route": "/add-event"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-BYI7DNOK.js"
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
    'index.csr.html': {size: 29299, hash: '54381167ba6470cb5ccf31ad5f09226a7b2a9e4f8d27af6dee5c0b3ff8af87a5', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '7765f060ee1d72250ee4ebced86778de176e77fab48c73d6b4a68867a92b1683', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: '012c7780f407b90315883b66012eba03e372c2b6c060ca058c6aa1b267e78cac', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '87617d2ae8f69f52051981031182481df1ed96fca12385d8dbc4ec805aea04e5', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '1ff8e481bb995134130c2786bf064b6e0c6c054ad58a11c43a6bd03870be830e', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '670133146195710fa01174feb46d9d7745f8c2be8bff18f84d9c17b55a4cebd3', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '89083d78a47dfe1b33eb6f6071a42277dadccbb9fdad5c5e99443c0effc974ea', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: '76f009e91343c6141a34cf91cb14a070a50fcd5f73490e23deb1f57a78f3956f', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: 'be69c44f2636dd1dc174c517cfd2e8ac941af6db731710589232d103052d053f', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: 'e85231384db20c1f6b2ef578961faebde1564ebccc42e437df5c2c1a39aed88f', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: '48bd79149a6dd234b5f0daa3a4c78ce9ddb8052a5e0b5903b7749fdb4fa8d2a9', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: '1baf3114464c9e1fc0f6ae5896d7ce30842947db38f48fd926b0e27423e0fbb6', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '5e1a658cc5fe2c1e50d58baaa546fc065a44430f72997723027115eea67e4bb1', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '86b36d6b92ded1a55fa1be3a550b42cd702af0aef6d6d2af11210e33b405eb57', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: 'f55baa8f5c59e5134ebd0c2430d3ca79a0a439f866878f6068d902b274b4bde0', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: 'b56f44c604ecf01bd94404d3b52c3394e6a65cd9ad87527b87374fa05e83d963', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-OGWMDQSA.css': {size: 330034, hash: 'S3EUQNflFf0', text: () => import('./assets-chunks/styles-OGWMDQSA_css.mjs').then(m => m.default)}
  },
};
