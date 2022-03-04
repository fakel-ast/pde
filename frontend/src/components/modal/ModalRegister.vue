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
          <input class="modal__input form-input" placeholder="Имя пользователя" type="text" name="username"/>
        </div>
        <div class="modal__row">
          <input class="modal__input form-input" placeholder="E-mail" type="text" name="email"/>
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
          />
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
import VueNextSelect from "vue-next-select";
import "vue-next-select/dist/index.min.css";

export default {
  name: "ModalRegister",
  components: {
    ModalBase,
    VueNextSelect,
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
      group: {},
      groups: [
        { title: "ОИБ-418", id: 1 },
        { title: "ОИБ-318", id: 2 },
        { title: "ОИБ-218", id: 3 },
      ],
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

.vue-select {
  width: 100%;
  padding: toRem(11) toRem(24) toRem(8) toRem(24);
  border: 1px solid $grey-color;
  border-radius: toRem(25);
  background-color: transparent;
  outline: none;
  font-size: toRem(22);
  line-height: toRem(25);
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
  border-radius: 5px;
  box-sizing: border-box;
  background: #ddd;

  &-item {
    padding: toRem(10);
    text-align: left;

    &:hover {
      background-color: #ebedef !important;
    }

    &:not(:last-child) {
      border-bottom: 1px solid #ccc;
    }


    &.selected {
      background-color: transparent !important;
    }

    &.highlighted {
      background-color: transparent;

    }
  }
}
</style>
