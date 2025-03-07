import { createRouter, createWebHistory } from 'vue-router'
import FormView from '../components/FormView.vue'
import ListView from '../components/ListView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: FormView
    },
    {
      path: '/list',
      component: ListView
    }
  ]
})

export default router