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
            {{ usernameError }}
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
        </div>
        <div class="modal__row">
          <input class="modal__input form-input" placeholder="Пароль" type="password" name="password"/>
        </div>
      </form>

    </template>
    <template #modal-confirm>
      <div class="modal__confirm">
        <button class="modal__button button">
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
      groups: [
        { title: "ОИБ-418", id: 1 },
        { title: "ОИБ-318", id: 2 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
        { title: "ОИБ-218", id: 3 },
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
        this.fioError = "Введите имя";
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
  computed: {
    isValidForm() {
      this.fioValidation();
      this.phoneValidation();
      this.emailValidation();
      this.addressValidation();
      this.commentValidation();
      return !(this.fioError.length || this.phoneError.length || this.emailError.length || this.addressError.length || this.commentValidation.length);
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
