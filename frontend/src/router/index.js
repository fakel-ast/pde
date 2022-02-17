import { createRouter, createWebHistory } from "vue-router";
import Categories from "@/views/Categories";

const routes = [
  {
    path: "/",
    name: "Categories",
    component: Categories,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
