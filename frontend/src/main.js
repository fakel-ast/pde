import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const app = createApp(App);
app.config.globalProperties.$host = process.env.NODE_ENV === "production" ? "/" : "http://localhost:5000/";
app.use(store).use(router).mount("#app");
