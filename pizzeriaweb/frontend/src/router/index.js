import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import CIForm from '@/components/CIForm'
import UserData from '@/components/UserData'
import OrderPizzas from '@/components/OrderPizzas'
import OrderResult from '@/components/OrderResult'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/order',
      name: 'CIForm',
      component: CIForm,
    }, 
    {
      path: "/order/:id",
      name: "UserData",
      component: UserData,
    },{
      path: '/order/:id/pizzas',
      name: "OrderPizzas",
      component: OrderPizzas,
    },
    {
      path: '/order/:id/bill',
      name: "OrderResult",
      component: OrderResult,
    },
    {
      path: "*",
      name: "not-found",
      redirect: "/",
    },
  ],
  mode: "history"
})
