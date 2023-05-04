// Composables
import { createRouter, createWebHistory } from 'vue-router'
import { useTrainStore } from '@/store/train'

const routes = [{
  path: '/',
  component: () => import('@/layouts/default/Default.vue'),
  children: [{
    path: '',
    name: 'train',
    component: () => import(/* webpackChunkName: "train" */ '@/views/Train.vue'),
  }]
}, {
  path: '/:id',
  component: () => import('@/layouts/default/Default.vue'),
  children: [{
    path: '',
    name: 'train-schedule',
    component: () => import(/* webpackChunkName: "train" */ '@/views/Train.vue'),
  }]
}]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from) => {
  const trainStore = useTrainStore()

  if (!from.name) {
    trainStore.loadTrains()
  }

  if (to.name === "train-schedule") {
    trainStore.loadTrainSchedule(to.params.id as string)
  }
})

export default router
