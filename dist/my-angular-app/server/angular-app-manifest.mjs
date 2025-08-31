
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
      "chunk-HLMNNQKO.js"
    ],
    "route": "/login"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-COIFM4DV.js"
    ],
    "route": "/files"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-LWTGG4XC.js"
    ],
    "route": "/homepage"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EXAEFVCT.js",
      "chunk-A5BWFRMV.js"
    ],
    "route": "/images"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-MBI65FOJ.js",
      "chunk-A5BWFRMV.js",
      "chunk-3EJB25IW.js",
      "chunk-WAP5QLUU.js"
    ],
    "route": "/dashboard"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-DYW5PP2Z.js",
      "chunk-57J56NDR.js"
    ],
    "route": "/news"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-VB5AHMFP.js",
      "chunk-57J56NDR.js"
    ],
    "route": "/news/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-ZY3D2O62.js",
      "chunk-57J56NDR.js"
    ],
    "route": "/edit-news/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-YVN5U2BE.js",
      "chunk-57J56NDR.js"
    ],
    "route": "/add-news"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-OISZDGC4.js",
      "chunk-R37ZHE5R.js"
    ],
    "route": "/tradition"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-2OJN4F5K.js",
      "chunk-R37ZHE5R.js"
    ],
    "route": "/tradition/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-QES4752E.js",
      "chunk-R37ZHE5R.js"
    ],
    "route": "/edit-tradition/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-YK7OWSHG.js",
      "chunk-R37ZHE5R.js"
    ],
    "route": "/add-tradition"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-6KRLIWY2.js",
      "chunk-WAP5QLUU.js"
    ],
    "route": "/events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-RPWSPJOI.js",
      "chunk-3EJB25IW.js",
      "chunk-WAP5QLUU.js"
    ],
    "route": "/admin-events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-5B2CPQYY.js"
    ],
    "route": "/contact"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-4JAZKV5P.js",
      "chunk-WAP5QLUU.js"
    ],
    "route": "/add-event"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EDOZRHKI.js"
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
    'index.csr.html': {size: 29299, hash: 'b96a84297e804b7e45e273e4f45eb933185e9b9824b7ae3cf4049cbc5915fd53', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '3b33440bc81737f3e67a5cc81763332972bc1c54b511d362d7fc552b75dec9fb', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '19a2b071d71874a2af2ef867a6a1dc20ffbe8cde95533be802a8a93115e5790f', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: 'cd8ea19015843f40a5347357858daee999ae045932dfaa2f0801291d6c5a2a34', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: 'c9d5a05fe301ebbfeb404e151fc439083aff64b806bb8cb23ee94f09ebf9eb19', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: '30e3b178f487b603af44752c899a1bad8d9808f247f8348472ef2fd189e6b380', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '2131f278fd344346279ef3a0f33ff0e8770888f3b56a5339b07afb1dbe20f7de', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: '9ba2e5b5db2be48b3035f6d31bd1770b94038d14a80549b8d0cf8fcf8c8165bb', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: 'cf42ff645f5ea12db73445b0e35e4c8679a1809c2bde5618dce2e329681d7a1b', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: '0005324b55b02fd565139947508c9c87464167dfcbe6e95220aef84fef7e00a4', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: 'd74d7edb0b1a91d9d6254766f233d02f45fc437ed41fed6fb6e47828b3a6b96d', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: '9e6ede31b49339183cd70a12438b94fd7e8e1a9233a49ef587a6295edda45a5e', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: 'a3697295b0b12a1aa85e5968c8de8463401fa97c7a2564bc4caa8374a02f29e9', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: 'a77319f14c8e449f326923b83bd9a120e69d5a43e8f000c439e655ce4bf7d329', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '9c85b8c5b92fdb5714fe40476c542144a3c1da95782a64c0f8eb9c2cbbd48c9a', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '0214fa3af09b995892db5f7ca1e4b51b8d32c4df4da13d23cdbb9decf439f85d', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-FOAOTY4F.css': {size: 329941, hash: 'Mi+gaaif+vg', text: () => import('./assets-chunks/styles-FOAOTY4F_css.mjs').then(m => m.default)}
  },
};
