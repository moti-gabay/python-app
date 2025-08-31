
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
      "chunk-FOWZHGWN.js"
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
    'index.csr.html': {size: 29299, hash: 'a76a9d8d4a7af6e4b23c3b7f2ebfb508e5c94c97dc9b9a41982315ba5d5b2831', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '60bc10c8c94ee80ff83ca525a58d867a9bda532e9456c5237ee44d1f7387a635', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: '2fdd3cf53d737e5924366657e260baa9faf77013d19f104c6e8167ce29061146', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '03a58df14abefd6ce7f30a3af64581cfac08422ea3c4d9d3b8c213c1d0ecffc7', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: 'ae13c8bfaf59558a13ffa60ae7ff8b1ce9906c5e2dab6c9d5a7c03c905de0227', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '471073840d46616a5fbfcc2f3b989bd4718be9499fde4dc93d94927892c12b55', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '9e39442fa960a00c547eb0f2ccdc1c44a4737ef0eab4fa6491d9070ca911176c', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '70bde0ad6a280dc1557cb047abfa1abe4527242b41f5454bfb8820d47657bc18', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: 'cc21f7b6a03c02eda62fb5d9162dd45e903d02a597856ee54c2b77d4050e327e', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: '9b3eaebbdd2d84c46ca70b693bb777cdb7f645b3dc3eea16aa39583fe0709a99', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: '2d65993248ec67a1097bdd2350700b9496ba30f5b85e3ed8f346bdcd75b77355', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '511d95115b59341e0ba2982686d05cc7569b7b3bd2734a58b5f9b0fc2bb6837f', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '4a83cdc365d22d52f9d8c1124a8ae0b962218a4c0af9c3dee287f9cf3c7bc2e0', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: '387a1f91279a199f8f1530f09b14615f829781e60175be23d3d32843392bd14d', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: '9b88be3a94f7b271ea794a9da7df9c080a2711c0ee21800f7a7ec53a9c255f92', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '15bca15bed4b806b24fce3da5ae09d7f7561bb9a648fdea570e9673ad766915d', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-OGWMDQSA.css': {size: 330034, hash: 'S3EUQNflFf0', text: () => import('./assets-chunks/styles-OGWMDQSA_css.mjs').then(m => m.default)}
  },
};
