import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Tasks from '../views/Tasks.vue'
import SingUp from '../views/SingUp.vue'
import SingIn from '../views/SingIn.vue'

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
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})


export default router
