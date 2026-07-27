/// <reference types="vite/client" />
declare module 'vuetify/*';
declare module 'vuetify/labs/*';
declare module 'vuetify/components/*';
declare module 'pinia';
declare module 'vue';
declare module 'vite';
declare module 'vite-plugin-vue-devtools';
declare module 'plotly.js-dist-min' {
  import * as Plotly from 'plotly.js-dist-min';
  export = Plotly;
}
