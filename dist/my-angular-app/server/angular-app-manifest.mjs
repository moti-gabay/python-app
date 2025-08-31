
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
    'index.csr.html': {size: 29299, hash: 'c484f43b1178d6279c6343c7c2dd6225535d5d60807c5a8ba788d9f2b0c53488', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '9b0ab221b4c34eeab089f650edce3adf65d937c117b8e787b191442db8a36287', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: '704569a0f10566c09f30c1c7391e5e685af19a0933e2dc5fec65fe5b50b9c93b', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: 'dc9b59a89d80d1f9956518a070225bfb80da22fceff0720609fd2b0dc7208912', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '7a747d76cf89f70f02e88c149ca545ecedec13489961f6659484e801428bc558', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '7a8ed4062e28d6e99aa4e4588e0e2950c49e59b17bae3cd67ab1c14bffe60bd7', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: 'a9463227d63a303223a48f0097486136175c0389b21121ed7a8a0d68b1a1c68d', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: 'f9fd3d98939308e181dadf9d934dbd3f954bc8aef3a871130a983947aafca539', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: 'cbefc0c88cb796ee6749e2a91b115f04cdc2dfe431ccf6f1dc1ddadc2352340c', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: 'e1036e9233a1ee86632f206e15e1c8d0cac491086d15d6c1d2d87191d270304b', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: 'a9e12d24981f3492d3f80c1972c39b43242a337251baf5ad7822b0979950cb83', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: '664182a5cfa6b5915f7ab345ee012d864ea94fe187a9e1101a17bd87209543e3', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '1c39232102c66b2800b4c2f89bace81ffeca980c82f0a861984ce8b607dbaa20', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: 'a1eb3d1431c3e35d1c4c8294affdff6b7ec389178ee81a9837b3639456833d96', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '1651cb4efde456789c28eedb896a2cd4923c40e27d662c4b0ae2d53518cca179', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: '06a81b1ae221b6063be25a17f0142fe96a5124068d7db629eb63b02c19a634fd', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'styles-FOAOTY4F.css': {size: 329941, hash: 'Mi+gaaif+vg', text: () => import('./assets-chunks/styles-FOAOTY4F_css.mjs').then(m => m.default)}
  },
};
