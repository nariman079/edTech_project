import AuthPage from '@/pages/AuthPage.vue';
import MainPage from '@/pages/MainPage.vue';
import ProfilPage from '@/pages/ProfilPage.vue';

import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/login', name: 'Login', component: AuthPage },
  { path: '/profile', name: 'Profile', component: ProfilPage},
  { path: '/', name: 'Main', component: MainPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // Если есть сохранённая позиция (например, при использовании кнопки "Назад")
    if (savedPosition) {
      return savedPosition;
    } else {
      // Перемещаем страницу к началу
      return { top: 0 };
    }
  },
});

export default router;