import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Tasks from '@/views/Tasks.vue';
import SingUp from '@/views/SingUp.vue';
import SingIn from '@/views/SingIn.vue';
import Categories from "@/views/Categories";
import Rating from "@/views/Rating";
import Profile from "@/views/Profile";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks
  },
  {
    path: '/sign-up',
    name: 'SingUp',
    component: SingUp
  },
  {
    path: '/sign-in',
    name: 'SingIn',
    component: SingIn
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/rating',
    name: 'Rating',
    component: Rating
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})


export default router
