import { createRouter, createWebHistory } from "vue-router";
import Categories from "@/views/Categories";
import Category from "@/views/Category";

const routes = [
  {
    path: "/",
    name: "Categories",
    component: Categories
  },
  {
    path: "/:categorySlug",
    name: "Category",
    component: Category
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
