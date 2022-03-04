<template>
  <modal-base ref="modalBase">
    <template #modal-error></template>
    <template #modal-success>

    </template>
    <template #modal-title>
      <span class="modal__header-active">Войти /</span> <span>Регистрация</span>
    </template>

    <template #modal-content>
      <form class="modal__form">
        <div class="modal__row">
          <input class="modal__input form-input" placeholder="Имя пользователя" type="text" name="username"/>
        </div>
        <div class="modal__row">
          <input class="modal__input form-input" placeholder="Пароль" type="text" name="password"/>
        </div>
      </form>

      <p class="modal__text forgot-password">
        Забыли пароль?
      </p>

    </template>
    <template #modal-confirm>
      <div class="modal__confirm">
        <button class="modal__button button">Войти</button>
      </div>
      <p class="link modal__another-modal">
        Регистрация
      </p>
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
    getTranslateJsonField: Function,
    wordTranslation: Function,
  },
  data() {
    return {
      username: "",
      usernameError: "",
      password: "",
      passwordError: "",
    };
  },
  methods: {
    open() {
      return this.$refs.modalBase.open();
    },
    close() {
      return this.$refs.modalBase.close();
    },
    fioValidation() {
      if (!this.fio.length) {
        this.fioError = "Enter fio TRANSLATE SUKA";
        return false;
      }
      this.fioError = "";
      return true;
    },
    phoneValidation() {
      if (!this.phoneObject.valid) {
        this.phoneError = "asdsad TRANSLATE SUKA";
        return false;
      }
      this.phoneError = "";
      return true;
    },
    modalValidation() {
      this.fioValidation();
      this.phoneValidation();
      if (!this.phoneError.length && !this.fioError.length) {
        return this.$refs.modalBase.confirm({
          fio: this.fio, phone: this.phoneObject.formatted, text: this.comment,
          variants_execution_id: this.activeVariant,
        });
      }
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

  &__form {
    margin-bottom: toRemMob(22);
    @include _desktop {
      margin-bottom: toRemMob(25);
    }
  }

  &__row {
    &:not(:last-child) {
      margin-bottom: toRemMob(22);
      @include _desktop {
        margin-bottom: toRemMob(25);
      }
    }
  }

  &__confirm {
    margin-top: toRemMob(30);
    @include _desktop {
      margin-top: toRem(30);
    }
  }

  &__another-modal {
    margin-top: toRemMob(30);
    @include _desktop {
      margin-top: toRem(31);
    }
  }
}

.forgot-password {
  cursor: pointer;
}
</style>
