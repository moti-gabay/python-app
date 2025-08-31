
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
      "chunk-KG6X2Z4S.js"
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
    'index.csr.html': {size: 29299, hash: '24159a672f47ce8d1fe9d32389849db2b06189b8a55d4cde6eb51d6095dfe4b9', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: 'ee721720890b2c65d6b07a00810958d2ccfcf4e22c4a7a61c69bb0443dcbf44a', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: '20b0c02eaca046d3918d9e2cb58a6a1dba2eab478a22ab412cbeb797d67fe7e8', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: 'db7992a326056191bf22b0d11a1d4a7f36caeaf302d1e0d2d87141b4c490d4c3', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: '98091223327d87712db7b21c91867394ef9be948041a072b0d4a96a0a81ba448', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: 'c1cc0aeaf63d3468d37ed735ddcf9e3ec94c039d9c20c197958c2432225a7d94', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '8bb523e9c68a77f6169eb97656c5cd6f94a3b8d110ba4a41517e8298fc6719d6', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: 'e6743c7f731417fdc1fe65fd3b3093f54d60bf236b64d92b5adfc7d042111732', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: '75004fbaba1dacba80350e842b92f2c0f9effa355f20ab6c5313d950bb9d80e7', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: 'f0a920223042e87f8c4e045237bb730f7ddecce6df79f08abc198cd58ce8735f', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: '580206f4e8bea93473c9c1ce71f32aae3dfd49a11e5c1ed1b86a566535210915', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: 'ea874b4d26740e1ecfc34fa324821c3603e5e295567a215a5cfa758164182656', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '1629fd70717d0b85080b781935ef4f1c65b558240884cfedfc58d28902c0d266', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '6925cd4ffb6b326136b305e6a643a6e71432c7a4a73e1d681ce66944decbbf89', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: '439c906eff32b31bebcab21ce4b4a96ebcdfeb28f91d328e0bba225554eecadd', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '2e7eceed83dc2abeec5375d30a192a3cb1d300bb3b0bae27b6454c5009d18604', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-FOAOTY4F.css': {size: 329941, hash: 'Mi+gaaif+vg', text: () => import('./assets-chunks/styles-FOAOTY4F_css.mjs').then(m => m.default)}
  },
};
