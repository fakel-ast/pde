<template>
  <modal-base ref="modalBase">
    <template #modal-error></template>
    <template #modal-success></template>
    <template #modal-title><span class="modal__header-active">Войти /</span> <span>Регистрация</span></template>

    <template #modal-content>
      <form class="modal__form">
        <div class="modal__row">
          <input
            @input="authError = ''"
            v-model="username"
            class="modal__input form-input"
            placeholder="Имя пользователя"
            type="text"
            name="username"
          />
          <div class="modal__error" v-if="usernameError.length">
            {{ usernameError }}
          </div>
        </div>
        <div class="modal__row">
          <input
            @input="authError = ''"
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

      <div class="forgot-password">
        <p class="modal__text">Забыли пароль?</p>
        <div class="modal__error modal__auth-error" v-if="authError.length">
          {{ authError }}
        </div>
      </div>
    </template>
    <template #modal-confirm>
      <div class="modal__confirm">
        <button @click="confirm" class="modal__button button">Войти</button>
      </div>
      <p @click="openModalRegister" class="link modal__another-modal">Регистрация</p>
    </template>
  </modal-base>
</template>

<script>
import ModalBase from "@/components/modal/ModalBase";

export default {
  name: "ModalLogin",
  components: {
    ModalBase,
  },
  props: {
    openModalRegister: Function,
  },
  data() {
    return {
      username: "",
      usernameError: "",
      password: "",
      passwordError: "",
      authError: "",
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
      if (!this.regexValidation(/^[\w \-А-я _]{1,128}$/, this.username)) {
        this.usernameError = "Некорректное имя пользователя";
        return false;
      }
      this.usernameError = "";
      return true;
    },
    passwordValidation() {
      this.passwordError = "";
      return true;
    },
    confirm() {
      if (!this.isValidForm) return;
      return this.$refs.modalBase.confirm({
        username: this.username,
        password: this.password,
      });
    },
    async showError() {
      return new Promise((resolve) => {
        this.$refs.modalBase.showError();
        setTimeout(() => {
          this.$refs.modalBase.hideError();
          resolve();
        }, 1000);
      });
    },
    async showSuccess() {
      return new Promise((resolve) => {
        this.$refs.modalBase.showSuccess();
        this.username = "";
        this.password = "";
        this.$refs.modalBase.hideSuccess();
        this.$refs.modalBase.close();
        resolve();
      });
    },
    notValidAuthData(errorText) {
      this.authError = errorText || "Неверные логи или пароль";
    },
  },
  computed: {
    isValidForm() {
      this.usernameValidation();
      this.passwordValidation();
      return !(this.usernameError.length || this.passwordError.length);
    },
  },
};
</script>

<style lang="scss">
.modal {
  &__auth-error {
    left: 0;
    right: 0;
  }
}

.forgot-password {
  position: relative;
  cursor: pointer;
}
</style>
