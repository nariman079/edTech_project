import AuthPage from '@/pages/AuthPage.vue';
import MainPage from '@/pages/MainPage.vue';

import { createRouter, createWebHistory } from 'vue-router';



const routes = [
  { path: '/login', name: 'Login', component: AuthPage },
  { path: '/', name: 'Main', component: MainPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;