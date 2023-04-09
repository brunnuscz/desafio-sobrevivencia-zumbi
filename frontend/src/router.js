import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", redirect: '/index' },
    { path: "/create", name: "create", component: () => import("./components/Createitem.vue") },
    { path: "/edit/:id", name: "edit", component: () => import("./components/EditItem.vue") },
    { path: "/index", name: "index", component: () => import("./components/Home.vue") },
    { path: "/items/", name: "items", component: () => import("./components/ListItem.vue") },
    { path: "/survivors/", name: "survivors", component: () => import("./components/ListSurvivor.vue") },
    { path: "/register/", name: "register", component: () => import("./components/Register.vue") },
    { path: "/inventories/", name: "inventories", component: () => import("./components/ListInventory.vue") },
  ]
});
