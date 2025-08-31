
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
      "chunk-FFDHG2EX.js"
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
    'index.csr.html': {size: 29299, hash: '5e6b0dc1e68dbe6fde1f2f8347b8dd0fbf5a12a701f2d5cc94544c745a7c4eec', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 17452, hash: '801bd0a3e1bfdbb6711b72a8f2179fe2b6b9eea8164379136bd986e50f9df6e7', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'add-news/index.html': {size: 38730, hash: '14fc6a05762c77e7d031fde1ddbc34ba0b7ae13007491cb7ecea05342b7db662', text: () => import('./assets-chunks/add-news_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 38678, hash: 'c15d972bbcdfe7d36ee03af19ce1cb0291996ef656662a6a1e6fdd8808ff75ee', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'files/index.html': {size: 38678, hash: 'fc81c10fd29b06cd7bfdbcfe6356daa6074f1a286ba7ddc20d5c6133234d8151', text: () => import('./assets-chunks/files_index_html.mjs').then(m => m.default)},
    'admin-events/index.html': {size: 38782, hash: '2a8e4353ac20ddc93780c857ea7ba51913e6593a1196ccafa9a0a4e05f0b59c4', text: () => import('./assets-chunks/admin-events_index_html.mjs').then(m => m.default)},
    'news/index.html': {size: 38730, hash: '3d8c72b2ec9c8b76a654c2c67d877f6fa741503d210cab6c469752fd16337e58', text: () => import('./assets-chunks/news_index_html.mjs').then(m => m.default)},
    'add-event/index.html': {size: 38730, hash: '6d7b35073ae1ed84af88f3fc196c60333cc35749e600bb7b719d93ef8aa46458', text: () => import('./assets-chunks/add-event_index_html.mjs').then(m => m.default)},
    'homepage/index.html': {size: 38678, hash: '282ca3e17d37814f68e9fa135159392316e5c71229197f74757753c592b6bf31', text: () => import('./assets-chunks/homepage_index_html.mjs').then(m => m.default)},
    'add-tradition/index.html': {size: 38730, hash: '718dcd34aa3efcfbe7bdaa2d3bf8db49ce7554a985dc23a27d84acec81b513d4', text: () => import('./assets-chunks/add-tradition_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 38678, hash: '749651824f04837c8acf7fa121cc554822371ed988b6b74ac0d1753b5615a046', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'images/index.html': {size: 38730, hash: '85be0452bc11d786cfb3eff3f7a9648a4ac8543eba41046a4557a3e4a9b94144', text: () => import('./assets-chunks/images_index_html.mjs').then(m => m.default)},
    'dashboard/index.html': {size: 38834, hash: '7446e73e83caeb021912a28c04a1e85db0d5dac08b50149fcd90701988dc162e', text: () => import('./assets-chunks/dashboard_index_html.mjs').then(m => m.default)},
    'tradition/index.html': {size: 38730, hash: '045f04c45c67176a31c1206fc867b4a4ac97aae329227c762784f056b608f8c9', text: () => import('./assets-chunks/tradition_index_html.mjs').then(m => m.default)},
    'events/index.html': {size: 38730, hash: '50e3a821a3b76074ec44c13b9ce18899dc067e9970482d6f4fbf72006c57ba43', text: () => import('./assets-chunks/events_index_html.mjs').then(m => m.default)},
    'donation/index.html': {size: 38678, hash: '7e89d0963ed82900fca64c8c0ce851e6e9e84cdf4f95db274be08f9ecd39f779', text: () => import('./assets-chunks/donation_index_html.mjs').then(m => m.default)},
    'styles-OGWMDQSA.css': {size: 330034, hash: 'S3EUQNflFf0', text: () => import('./assets-chunks/styles-OGWMDQSA_css.mjs').then(m => m.default)}
  },
};
