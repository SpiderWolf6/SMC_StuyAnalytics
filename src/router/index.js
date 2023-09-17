import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/soccer',
    name: 'soccer',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "soccer" */ "../views/SoccerView.vue"),
  },
  {
    path: "/metrics",
    name: "metrics",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "metrics" */ "../views/MetricsView.vue"),
  },
  {
    path: "/squad",
    name: "squad",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "squad" */ "../views/SquadView.vue"),
  },
  {
    path: "/dates",
    name: "dates",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "dates" */ "../views/DatesView.vue"),
  },
  {
    path: "/graph",
    name: "graph",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "graph" */ "../views/GraphView.vue"),
  },
]

const router = new VueRouter({
  routes
})

export default router
