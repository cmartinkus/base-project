import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import '@mdi/font/css/materialdesignicons.css'; // Import MDI icons
import 'vuetify/styles'; // Import Vuetify styles
import * as components from 'vuetify/components';
import * as labsComponents from 'vuetify/labs/components';
import { createVuetify } from 'vuetify';

import App from './App.vue'
import router from './router'

const app = createApp(App)

const vuetify = createVuetify({
  components: {
    ...components,
    ...labsComponents,
  },
  theme: {
    defaultTheme: 'dark',
  },
})




app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
