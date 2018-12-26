import Vue from 'vue'
import Router from 'vue-router'
import Chats from '@/components/Chats'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Room from '@/components/rooms/Room'
import Dialog from '@/components/rooms/Dialog'

var pathToRegexp = require('path-to-regexp')

Vue.use(Router)
var pattern = "/^((http?|ftp|smtp):\/\/)?(www.)?/[0-9A-Za-z]/";

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chats
    },
    {
      path: '/room',
      name: 'room',
      component: Room
    },
    {
      path: '/dialog',
      name: 'dialog',
      component: Dialog
    },
    {
      path: '/login/*',
      name: 'login',
      component: Login
    },
  ]
})
