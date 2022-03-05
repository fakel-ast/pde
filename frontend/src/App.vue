<template>
  <header-component :open-modal-login="openModalLogin"/>
  <modal-login
    ref="modalLogin"
    :open-modal-register="openModalRegister"

  />
  <modal-register
    ref="modalRegister"
    :open-modal-login="openModalLogin"
  />
  <router-view
    :categories="categories"
    :get-solved-suffix="getSolvedSuffix"
    :get-users-suffix="getUsersSuffix"
  />
  <footer-component :categories="categories"/>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";
import ModalLogin from "@/components/modal/ModalLogin";
import ModalRegister from "@/components/modal/ModalRegister";
import {Axios} from "@/assets/js/http-common";

export default {
  name: "App",
  components: {
    FooterComponent,
    HeaderComponent,
    ModalLogin,
    ModalRegister,
  },
  created() {
    this.getCategories();
  },
  data() {
    return {
      categories: [],
    };
  },
  methods: {
    async getCategories() {
      try {
        const { data } = await Axios.get("categories/");
        this.categories = data?.categories || [];
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
    async sendModalLogin(data) {
      console.log(data);
    },
    async sendModalRegister(data) {
      console.log(data);
    },
    async openModalLogin() {
      this.$refs.modalRegister.close();
      const modalResult = await this.$refs.modalLogin.open();
      if (modalResult && Object.entries(modalResult).length) {
        // Fake send form to backend
        const result = await this.sendModalLogin(modalResult);
        // if success back response show success and close modal, else show error
        if (result) {
          await this.$refs.modalLogin.showSuccess();
        } else {
          await this.$refs.modalLogin.showError();
          // Тут костыль небольшой. Что бы повторить все эти действия, мы вызываем сам себя :)
          this.openModalLogin();
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

  &:hover {
    background: $blue-gradient;
  }

  &:active {
    background: $sea-color;
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
