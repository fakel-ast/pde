import { createRouter, createWebHistory } from "vue-router";
import { nextTick } from "vue";

import HomePage from "../views/HomePage";
import Categories from "../views/Categories";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
    meta: {
      title: "Админка"
    }
  },
  {
    path: "/categories",
    name: "Categories",
    component: Categories,
    meta: {
      title: "Категории задач"
    }
  },
];

const router = createRouter({
  history: createWebHistory("admin"),
  routes
});

router.beforeEach((to) => {
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  // see: https://router.vuejs.org/ru/guide/advanced/meta.html
  // see: https://v3.vuejs.org/guide/migration/global-api-treeshaking.html#_3-x-syntax
  nextTick(() => {
    document.title = to.meta?.title || "Админка";
  });
});


export default router;
