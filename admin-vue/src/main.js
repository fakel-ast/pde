import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'

const app = createApp(App);
app.config.globalProperties.$host = process.env.NODE_ENV === 'production' ? '/' : 'http://localhost:8000/';
app.config.globalProperties.$serverHost = process.env.NODE_ENV === 'production' ? '/' : 'https://greendi.com/';

// Кастомная хута для автофокуса при создании инпута
app.directive('focus', {
  // When the bound element is mounted into the DOM...
  mounted(el) {
    // Focus the element
    el.focus()
  }
})
app.use(ElementPlus).use(router).mount('#app')
