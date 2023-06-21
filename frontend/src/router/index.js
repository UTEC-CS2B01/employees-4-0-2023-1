import { createRouter, createWebHistory } from "vue-router";
import DepartmentCreationView from "@/views/DepartmentCreationView.vue";

const routes = [
  {
    path: "/",
    name: "DepartmentCreationIndex",
    component: DepartmentCreationView,
  },
  {
    path: "/department-creation",
    name: "DepartmentCreation",
    component: DepartmentCreationView,
  },
  {
    path: "/department-list",
    name: "DepartmentList",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DepartmentListView.vue"),
  },
  {
    path: "/employee-creation",
    name: "EmployeeCreation",
    component: () => import("@/views/EmployeeCreationView.vue"),
  },
  {
    path: "/employee-list",
    name: "EmployeeList",
    component: () => import("@/views/EmployeeListView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
