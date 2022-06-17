import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const app = createApp(App);
app.config.globalProperties.$host = process.env.NODE_ENV === "production" ? "/" : "http://localhost:5000/";
// Кастомная хута для автофокуса при создании инпута
app.directive("focus", {
  // When the bound element is mounted into the DOM...
  mounted(el) {
    // Focus the element
    el.focus();
  }
});
app.use(store).use(router).mount("#app");
