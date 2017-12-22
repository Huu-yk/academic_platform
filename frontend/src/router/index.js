import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      component: resolve => require(['../components/common/Home.vue'], resolve),
      children:[
              {
                  path: '/',
                  component: resolve => require(['../components/page/Home_page.vue'],resolve)
              },
              {
                  path: '/page1',
                  component: resolve => require(['../components/page/Temp_page1.vue'], resolve)
              },
              {
                  path: '/page2',
                  component: resolve => require(['../components/page/Temp_page2.vue'], resolve)
              }
      ]
    }
  ]
})
