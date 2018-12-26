// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import http from 'http';
import App from './App';
import router from './router';
import MuseUi from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
//import store from 'store'
//import VueSocketIo from 'vue-socket.io'
//import io from 'socket.io-client'

//var host = 'localhost';
//var nodejs_port = '4000';



//Vue.use(new VueSocketIo({
//	debug: true,
//	connection: io('http://' + host +':' + nodejs_port),
//	vuex:{
//		store,
//		actionPrefix: 'SOCKET_',
//		mutationPrefix: 'SOCKET_'
//	},
//	headers: {
//  	Authorization: 'Token ' + sessionStorage.getItem('auth_token'),
//  	}

//}));

Vue.config.productionTip = false
Vue.use(MuseUi);

/* eslint-disable no-new */
//new Vue({
//  el: '#app',
//  router,
//  socket,
//  components: { App },
//  template: '<App/>'
//});

new Vue({
    router,
    //store,
    render: h => h(App)
}).$mount('#app')


