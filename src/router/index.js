import { createRouter, createWebHistory } from "vue-router";
import Explore from "../views/Explore.vue";
import Home from "../views/Home.vue";
import QR from "../views/QR.vue";

const routes = [
  {
    path: "/",
    name: "Home_",
    component: Home,
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/explore",
    name: "Explore",
    component: Explore,
  },
  {
    path: "/qr",
    name: "QR",
    component: QR,
  }
];

const router = createRouter({
  mode: "history",
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
