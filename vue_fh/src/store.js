import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    allLots: []
  },
  getters: {
    lots: state => {
      return state.allLots
    }
  },
  mutations: {
    setAllLots (state, lots) {
      state.allLots = lots
    }
  },
  actions: {
    setAllLots ({ commit }, lots) {
      commit('setAllLots', lots)
    }
  }
});