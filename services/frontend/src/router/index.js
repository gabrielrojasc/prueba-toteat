import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView";
import OrderListView from "../views/OrderListView";
import OrderView from "@/views/OrderView";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/orders",
    name: "Orders",
    component: OrderListView,
  },
  {
    path: "/order/:id",
    name: "Order",
    component: OrderView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
