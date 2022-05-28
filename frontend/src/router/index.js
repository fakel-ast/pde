import { createRouter, createWebHistory } from "vue-router";
import Categories from "@/views/Categories";
import Category from "@/views/Category";
import TaskDetail from "@/views/TaskDetail";
import Profile from "@/views/Profile";
import RatingPage from "@/views/RatingPage";

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
  },
  {
    path: "/:categorySlug/:taskId",
    name: "TaskDetail",
    component: TaskDetail
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/top",
    name: "RatingPage",
    component: RatingPage
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
