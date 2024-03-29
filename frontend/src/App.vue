<template>
  <header-component :open-modal-login="openModalLogin" :logout="logout"/>
  <modal-login
    ref="modalLogin"
    :open-modal-register="openModalRegister"
  />
  <modal-register
    ref="modalRegister"
    :groups="groups"
    :open-modal-login="openModalLogin"
  />
  <router-view
    :categories="categories"
    :get-solved-suffix="getSolvedSuffix"
    :get-users-suffix="getUsersSuffix"
    :get-points-count-suffix="getPointsCountSuffix"
    :open-modal-login="openModalLogin"
    :get-answer-date="getAnswerDate"
    :logout="logout"
  />
  <footer-component :open-modal-login="openModalLogin" :categories="categories"/>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";
import ModalLogin from "@/components/modal/ModalLogin";
import ModalRegister from "@/components/modal/ModalRegister";
import {Axios} from "@/assets/js/http-common";
import {computed} from "vue";
import moment from "moment";

export default {
  name: "App",
  components: {
    FooterComponent,
    HeaderComponent,
    ModalLogin,
    ModalRegister,
  },
  provide() {
    return {
      deviceWidth: computed(() => this.deviceWidth),
    };
  },
  created() {
    this.getCurrentUser();
    this.getCategories();
    this.getGroups();
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.onResize);
  },
  data() {
    return {
      categories: [],
      groups: [],
      deviceWidth: window.innerWidth,
    };
  },
  methods: {
    async logout() {
      this.$store.commit("updateCurrentUser", {});
      try {
        await Axios.get("users/logout/");
      } catch (error) {
        console.log(error);
      }
    },
    async getCategories() {
      try {
        const { data } = await Axios.get("categories/");
        this.categories = data?.categories || [];
      } catch (error) {
        console.error(error);
      }
    },
    async getGroups() {
      try {
        const { data } = await Axios.get("groups/");
        this.groups = data?.groups || [];
      } catch (error) {
        console.error(error);
      }
    },
    async getCurrentUser() {
      try {
        const { data } = await Axios.get("users/current/");
        this.$store.commit("updateCurrentUser", data?.user || {});
      } catch (error) {
        console.error(error);
      }
    },
    getSolvedSuffix(count) {
      count = (count || 0).toString();
      if (count[count.length - 1] === "1" && count.slice(count.length - 2) !== "11") return "Решил";
      return "Решило";
    },
    getUsersSuffix(count) {
      count = (count || 0).toString();
      if (count[count.length - 1] === "1" && count.slice(count.length - 2) !== "11") return "пользователь";
      else if (["2", "3", "4"].includes(count[count.length - 1]) && !["12", "13", "14"].includes(count.slice(count.length - 2))) {
        return "пользователя";
      }
      return "пользователей";
    },
    getPointsCountSuffix(count) {
      count = (count || 0).toString();
      if (count[count.length - 1] === "1" && count.slice(count.length - 2) !== "11") return "очко";
      else if (["2", "3", "4"].includes(count[count.length - 1]) && !["11", "12", "13", "14"].includes(count.slice(count.length - 2))) {
        return "очка";
      }
      return "очков";
    },
    async sendModalLogin(dataToRequest) {
      try {
        const { data } = await Axios.post("users/login/", dataToRequest);
        this.$store.commit("updateCurrentUser", data?.user || {});
        return { success: !data?.errors, isReopen: data?.errors };
      } catch (error) {
        console.error(error);
        if (error?.response?.status === 400) {
          this.$refs.modalLogin.notValidAuthData();
          return { success: false, isReopen: true, isNotShowError: true };
        } else if (error?.response?.status === 403) {
          this.$refs.modalLogin.notValidAuthData("Попробуйте авторизоваться позже!");
          return { success: false, isReopen: true, isNotShowError: true };
        }
        return { success: false, isReopen: true };
      }
    },
    async sendModalRegister(dataToRequest) {
      try {
        const { data } = await Axios.post("users/", dataToRequest);
        this.$store.commit("updateCurrentUser", data?.user || {});
        return !data?.errors;
      } catch (error) {
        console.error(error);
      }
    },
    async openModalLogin() {
      this.$refs.modalRegister.close();
      const modalResult = await this.$refs.modalLogin.open();
      if (modalResult && Object.entries(modalResult).length) {
        // Fake send form to backend
        const result = await this.sendModalLogin(modalResult);
        console.log(result);
        // if success back response show success and close modal, else show error
        if (result?.success) {
          await this.$refs.modalLogin.showSuccess();
        } else {
          if (!result?.isNotShowError) {
            await this.$refs.modalLogin.showError(result?.message);
          }
          // Тут костыль небольшой. Что бы повторить все эти действия, мы вызываем сам себя :)
          if (result?.isReopen) this.openModalLogin();
        }
      }
    },
    async openModalRegister() {
      this.$refs.modalLogin.close();
      const modalResult = await this.$refs.modalRegister.open();
      if (modalResult && Object.entries(modalResult).length) {
        // Fake send form to backend
        const result = await this.sendModalRegister(modalResult);
        // if success back response show success and close modal, else show error
        if (result) {
          await this.$refs.modalRegister.showSuccess();
        } else {
          await this.$refs.modalRegister.showError();
          // Тут костыль небольшой. Что бы повторить все эти действия, мы вызываем сам себя :)
          this.openModalRegister();
        }
      }
    },
    onResize() {
      this.deviceWidth = window.innerWidth;
    },
    getAnswerDate(date) {
      return moment(date).locale("ru").format("DD:MM:YYYY в H:mm");
    },
  },
};
</script>

<style lang="scss">
@import "~reset-css";
@import "./assets/css/fonts";

* {
  box-sizing: border-box;
}

a {
  text-decoration: none;
  color: $white-color;
}


.link {
  cursor: pointer;
  transition: color .2s ease;

  &:active {
    color: $blue-color;
    text-decoration: underline;
  }

  &:hover {
    color: $blue-color;
    text-decoration: underline;
  }
}

html {
  line-height: 25px;
  font-size: 6vw;
  font-family: "TT Commons";
  @include _desktop {
    font-size: 1.15vw;
  }
  @include _max {
    font-size: 22.57px;
  }
}

body {
  background-color: $body-background;
  color: $white-color;
  font-weight: normal;
}

input {
  padding: 0;
  outline: none;
  border: none;
  background-image: none;
  background-color: transparent;
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
  font-family: "TT Commons";

  @include _desktop {
    font-size: toRem(22);
    line-height: toRem(25);
  }
}

.container {
  padding: 0 toRemMob(28);
  margin: 0 auto;

  @include _desktop {
    padding: 0 toRem(15);
    max-width: toRem(1350);
  }
}

.button {
  padding: toRem(10) toRem(37) toRem(8) toRem(37);
  border-radius: 40px;
  background: $blue-color;

  border: none;
  outline: none;
  cursor: pointer;
  color: $white-color;
  font-size: toRem(22);
  line-height: toRem(25);
  transition: background-color .4s ease;

  &:hover {
    background-color: $sea-color;
  }

  &:active {
    background-color: $sea-color;
  }

  &.button-red {
    transition: background-color .2s ease;

    background-color: $red-color;

    &:hover {
      background: #fe3a3a;
    }

    &:active {
      background: $red-color;
    }
  }

  &.disabled {
    cursor: auto;
    background: $grey-color;
  }
}

.page-title {
  font-size: toRemMob(25);
  line-height: toRemMob(29);
  margin-bottom: toRemMob(25);
  font-weight: 600;

  @include _desktop {
    font-size: toRem(86);
    line-height: toRemMob(99);
    margin-bottom: toRem(76.771);
  }
}

.only-desktop {
  @include _mobile {
    display: none;
  }
}

.only-mobile {
  @include _desktop {
    display: none;
  }
}

.success-text {
  color: $green-color;
}

.error-text {
  color: $red-color;
}

.form-input {
  flex-basis: 100%;
  width: 100%;
  padding: toRem(11) toRem(24) toRem(8) toRem(24);
  border: 1px solid $grey-color;
  border-radius: toRem(25);
  background-color: transparent;
  color: $white-color;
  outline: none;
  font-size: toRem(22);
  line-height: toRem(25);

  &::placeholder {
    color: $grey-color;
  }
}
</style>
