<template>
  <modal-base ref="modalBase">
    <template #modal-error></template>
    <template #modal-success>

    </template>
    <template #modal-title>
      <span>Войти</span> <span class="modal__header-active">/ Регистрация</span>
    </template>

    <template #modal-content>
      <form class="modal__form">
        <div class="modal__row">
          <input class="modal__input form-input" v-model="username" placeholder="Имя пользователя" type="text"
                 name="username"/>
          <div class="modal__error" v-if="usernameError.length">
            {{ usernameError }}
          </div>
        </div>
        <div class="modal__row">
          <input class="modal__input form-input" v-model="email" placeholder="E-mail" type="email" name="email"/>
          <div class="modal__error" v-if="emailError.length">
            {{ emailError }}
          </div>
        </div>
        <div class="modal__row">
          <vue-next-select
            v-model="group"
            :options="groups"
            :close-on-select="true"
            :empty-model-value="false"
            :min="1"
            placeholder="Группа"
            label-by="title"
            :class="{ active: group }"
          />
          <div class="modal__error" v-if="groupError.length">
            {{ groupError }}
          </div>
        </div>
        <div class="modal__row">
          <input
            @input="passwordValidation"
            v-model="password"
            class="modal__input form-input"
            placeholder="Пароль"
            type="password"
            name="password"
          />
          <div class="modal__error" v-if="passwordError.length">
            {{ passwordError }}
          </div>
        </div>
      </form>

    </template>
    <template #modal-confirm>
      <div class="modal__confirm">
        <button @click="confirm" class="modal__button button">
          Зарегистрироваться
        </button>
      </div>
      <p @click="openModalLogin" class="link modal__another-modal">
        Уже есть аккаунт?
      </p>
    </template>
  </modal-base>
</template>

<script>

import ModalBase from "@/components/modal/ModalBase";
import VueNextSelect from "vue-next-select";
import "vue-next-select/dist/index.min.css";

export default {
  name: "ModalRegister",
  components: {
    ModalBase,
    VueNextSelect,
  },
  props: {
    openModalLogin: Function,
    groups: Array,
  },
  data() {
    return {
      username: "",
      usernameError: "",
      email: "",
      emailError: "",
      password: "",
      passwordError: "",
      group: null,
      groupError: "",
    };
  },
  methods: {
    open() {
      return this.$refs.modalBase.open();
    },
    close() {
      return this.$refs.modalBase.close();
    },
    regexValidation(re, str) {
      return re.test(str);
    },
    usernameValidation() {
      if (!this.regexValidation(/^[\w \-А-я_]{1,128}$/, this.username)) {
        this.usernameError = "Некорректное имя пользователя";
        return false;
      }
      this.usernameError = "";
      return true;
    },
    passwordValidation() {
      if (!this.regexValidation(/(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}/, this.password)) {
        this.passwordError = "Слабый пароль";
        return false;
      }
      this.passwordError = "";
      return true;
    },
    groupValidation() {
      if (!this.group || !Object.entries(this.group).length) {
        this.groupError = "Группа обязательное поле";
        return false;
      }
      this.groupError = "";
      return true;
    },
    emailValidation() {
      if (!this.regexValidation(/^([\wА-я.-]+)@([\w.-]+)\.([A-z]{1,10})$/, this.email)) {
        this.emailError = "Некорректный E-mail";
        return false;
      }
      this.emailError = "";
      return true;
    },
    confirm() {
      if (!this.isValidForm) return;
      return this.$refs.modalBase.confirm({
        username: this.username,
        email: this.email,
        group: this.group?.id,
        password: this.password,
      });
    },
    async showError() {
      return new Promise(resolve => {
        this.$refs.modalBase.showError();
        setTimeout(() => {
          this.$refs.modalBase.hideError();
          resolve();
        }, 1000);
      });
    },
    async showSuccess() {
      return new Promise(resolve => {
        this.$refs.modalBase.showSuccess();
        setTimeout(() => {
          this.fio = "";
          this.phone = "";
          this.comment = "";
          this.$refs.modalWindowMask.clearPhone();
          this.$refs.modalBase.hideSuccess();
          this.$refs.modalBase.close();
          resolve();
        }, 1000);
      });
    },
  },
  computed: {
    isValidForm() {
      this.usernameValidation();
      this.passwordValidation();
      this.emailValidation();
      this.groupValidation();
      return !(this.usernameError.length || this.passwordError.length || this.emailError.length || this.groupError.length);
    },
  },

};
</script>

<style lang="scss">
.modal {
  text-align: center;

  &__header {
    margin-bottom: toRem(30);
    @include _desktop {
      margin-bottom: toRem(41);
    }
  }
}

.forgot-password {
  cursor: pointer;
}

.vue-select {
  width: 100%;
  padding: toRem(11) toRem(24) toRem(8) toRem(24);
  border: 1px solid $grey-color;
  border-radius: toRem(25) !important;
  background-color: transparent;
  outline: none;
  font-size: toRem(22);
  line-height: toRem(25);

  &.active {
    border-color: $white-color;

    .icon.arrow-downward {
      border-color: $white-color;
    }
  }

  &.direction-top {
    .vue-dropdown {
      bottom: toRem(54);
    }
  }

  &.direction-bottom {
    .vue-dropdown {
      top: toRem(54);
    }
  }

}

.vue-input {
  input:not([placeholder="Группа"])::placeholder {
    color: $white-color;
  }

  input[placeholder="Группа"]::placeholder {
    color: $grey-color;
  }

}

.vue-dropdown {
  max-height: toRem(200) !important;
  padding: toRem(31) toRem(20) toRem(27) toRem(21);
  border-radius: toRem(19) !important;
  box-shadow: 5px 5px 17px 5px rgba(0, 0, 0, 0.15);
  border: none;
  border-right: toRem(16) solid transparent;
  box-sizing: border-box;
  background: $dark-grey-color;

  &::-webkit-scrollbar {
    width: 4px;
  }

  &::-webkit-scrollbar-track {
    margin-top: toRem(2);
    margin-bottom: toRem(2);
    background-color: transparent;
  }

  &::-webkit-scrollbar-thumb {
    //max-height: toRem(1);
    border: 5px solid $grey-color;
    border-radius: toRem(5);
    padding-top: 100px;
  }


  &-item {
    font-size: toRem(22);
    line-height: toRem(25);
    text-align: left;

    &:not(:last-child) {
      margin-bottom: toRem(34);
    }

    &:hover {
      color: $blue-color;
    }

    &.selected {
      background-color: transparent !important;
      color: $white-color;
    }

    &.highlighted {
      background-color: transparent;
    }
  }
}

.icon.arrow-downward {
  width: toRem(10);
  height: toRem(10);
  margin-top: toRem(-4);
  transform: rotate(-45deg);
  border: none;
  border-bottom: 1px solid $grey-color;
  border-left: 1px solid $grey-color;

  &.active {
    margin-top: toRem(6);
    transform: rotate(180-45deg);
  }
}
</style>
