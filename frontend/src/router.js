import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", redirect: '/index' },
    { path: "/create", name: "create", component: () => import("./components/Createitem.vue") },
    { path: "/edit/:id", name: "edit", component: () => import("./components/EditItem.vue") },
    { path: "/index", name: "index", component: () => import("./components/Home.vue") },
    { path: "/list/survivors/", name: "list_survivors", component: () => import("./components/ListSurvivor.vue") },
  ]
});
