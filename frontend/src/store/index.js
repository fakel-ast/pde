import { createStore } from "vuex";

export default createStore({
  state: {
    currentUser: {}
  },
  getters: {
    currentUser(state) {
      return state.currentUser;
    }
  },
  mutations: {
    updateCurrentUser(state, value) {
      state.currentUser = value;
    }
  },
  actions: {},
  modules: {}
});
