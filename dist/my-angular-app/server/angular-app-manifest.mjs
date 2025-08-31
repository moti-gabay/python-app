
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
      "chunk-SAL4WDIE.js"
    ],
    "route": "/login"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EJNLKIWR.js"
    ],
    "route": "/files"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-GKSJUGEC.js"
    ],
    "route": "/homepage"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-EWHLOY5I.js",
      "chunk-5NAYAW43.js"
    ],
    "route": "/images"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-L6XOLC3U.js",
      "chunk-5NAYAW43.js",
      "chunk-ZT2SYR3O.js",
      "chunk-SRXVNZZ4.js"
    ],
    "route": "/dashboard"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-XJKC6L6H.js",
      "chunk-BO4PLAYH.js"
    ],
    "route": "/news"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-IARFUW6J.js",
      "chunk-BO4PLAYH.js"
    ],
    "route": "/news/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-WPD63PNZ.js",
      "chunk-BO4PLAYH.js"
    ],
    "route": "/edit-news/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-BAIVE52V.js",
      "chunk-BO4PLAYH.js"
    ],
    "route": "/add-news"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-3C4FX3Z3.js",
      "chunk-QIK4J3BX.js"
    ],
    "route": "/tradition"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-YGYHV243.js",
      "chunk-QIK4J3BX.js"
    ],
    "route": "/tradition/*"
  },
  {
    "renderMode": 0,
    "preload": [
      "chunk-KF2EMHD4.js",
      "chunk-QIK4J3BX.js"
    ],
    "route": "/edit-tradition/*"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-UOXKHLWP.js",
      "chunk-QIK4J3BX.js"
    ],
    "route": "/add-tradition"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-IUBAK63L.js",
      "chunk-SRXVNZZ4.js"
    ],
    "route": "/events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-PYDFHS7H.js",
      "chunk-ZT2SYR3O.js",
      "chunk-SRXVNZZ4.js"
    ],
    "route": "/admin-events"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-ZJQQTRLF.js"
    ],
    "route": "/contact"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-ESUAMZRV.js",
      "chunk-SRXVNZZ4.js"
    ],
    "route": "/add-event"
  },
  {
    "renderMode": 2,
    "preload": [
      "chunk-ZZB5NRH5.js"
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
    'index.csr.html': {size: 29299, hash: '9e0e8dca05f91edc9c9584618e1b46ed47352a160b0498b97bca9ac51df67cb2', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: 'bae05d67bdfe5dd0f768e547de6be7fb0bbe63f5a04cf502305f7e4c690c47ac', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '7859f9bae0c10e288d83c5d84d776894f39f12acaa4bd0f5d147cec2607f8dfc', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '8cdcd3cd77c68d58ba288598d4a2f0acaef33f55f36b5ff41a30d75914200605', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: '31d1f9967834d2cec282e64d7900cdfdbf74bce6f33ac52611d124d23d878827', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '5cd7409fb0275657e696d88b68a5aeb841d9e63703ab869c9566f28110c7bb2d', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: '851d60817a334c406b65e2356df46fb081102cb61988f9d99245c23629111931', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: 'feefadf0b503a813e555e446ea3acda70f7dd206dfed3427de83c2918dd8ec13', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '1233af4db182fc2d6ba16dd8101874b5d1a917ceacbe9fa90f4cb6be44641d2e', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: 'f8184becd8d7d46e738769a04937065f2e17e2029b81d6ca7ff1cb6927241749', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: '8d8e196c03d528c0461e28d64f37cb9c11212336694bc214056d89e77c8050f4', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: '6b9d0546a98b05eab5e0faf369a0459456060e71a3a26ae4cce6606888d06786', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: 'b7217e7745a43e9a540fa2ab0dd03819e58ae38645688e6970eccd13fcffe381', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '0f193d31134ae51aecc8f4d390b3d78fb833883179713343eee961481a7a96ea', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: 'efc9dfed11d8198b4a0072b5d45ba96c87b7df5e2dac7d214f66651af6f9d750', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '5ad62360775942e48f8d07f7fec5554740c132ec84040d77082ccfda3f4ebda3', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'styles-FOAOTY4F.css': {size: 329941, hash: 'Mi+gaaif+vg', text: () => import('./assets-chunks/styles-FOAOTY4F_css.mjs').then(m => m.default)}
  },
};
