<template>
  <div v-show="isOpen" @click="close" ref="modal" class="modal">
    <div @click.stop class="modal__body">
      <slot name="modal-error" v-if="isError">
        <div class="modal__send-error modal-error">
          <div class="modal-error__image"></div>
          <h2 class="modal-error__title">Ой!</h2>
          <p class="modal-error__description">
            Что-то пошло не так. Попробуйте повторить запрос.
          </p>
        </div>
      </slot>
      <slot name="modal-success" v-if="isSuccess"></slot>
      <div class="modal__header">
        <slot :close="close" name="modal-close">
          <div class="modal__close only-mobile">
            <div class="modal__close-close" @click="close"></div>
          </div>
        </slot>
        <h2 class="modal__title">
          <slot name="modal-title">
            Название модалки
          </slot>
        </h2>
      </div>
      <div class="modal__content">
        <slot name="modal-content">
          Modal content
        </slot>
      </div>
      <div class="modal__footer">
        <slot name="modal-actions">
          <slot
            :confirm="confirm"
            name="modal-confirm"
          >
            Отправить
          </slot>
        </slot>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  currentModalController: null,
  name: "ModalBase",
  emits: {
    close: null,
    open: null,
  },
  data() {
    return {
      isOpen: false,
      isError: false,
      isSuccess: false,
    };
  },
  components: {},
  methods: {
    async open() {
      let resolve;
      let reject;
      const modalPromise = new Promise((ok, fail) => {
        resolve = ok;
        reject = fail;
      });
      this.$options.currentModalController = { resolve, reject };
      this.isOpen = true;
      this.toggleBlockScroll(true);
      this.$emit("open");
      return modalPromise;
    },
    close() {
      this.toggleBlockScroll(false);
      this.$options.currentModalController?.resolve(false);
      this.isOpen = false;
      this.$emit("close");
    },
    confirm(modalData = null) {
      return this.$options.currentModalController.resolve(modalData);
    },
    showError() {
      this.isError = true;
    },
    hideError() {
      this.isError = false;
    },
    showSuccess() {
      this.isSuccess = true;
    },
    hideSuccess() {
      this.isSuccess = false;
    },
    toggleBlockScroll(isBlock) {
      const modal = this.$refs.modal;
      const htmlElement = document.documentElement;
      const lockPaddingValue = window.innerWidth - document.body.offsetWidth + "px";

      if (isBlock) {
        modal.style.paddingLeft = "0";
        htmlElement.style.overflow = "hidden";
        htmlElement.style.paddingRight = lockPaddingValue;

      } else {
        modal.style.paddingLeft = lockPaddingValue;
        htmlElement.style.overflow = "";
        htmlElement.style.paddingRight = "0px";
      }
    },
  },
};
</script>

<style lang="scss">
.modal {
  position: fixed;
  left: 0;
  top: 0;
  z-index: 4;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: $grey-color;
  background-color: rgba(0, 0, 0, .5);
  text-align: center;

  &__body {
    position: relative;
    width: 100%;
    height: 100%;
    padding: toRemMob(22) toRemMob(18) toRemMob(18) toRemMob(18);
    background-color: $dark-grey-color;

    @include _mobile {
      overflow: scroll;
    }

    @include _desktop {
      height: unset;
      width: unset;
      min-width: toRem(427);
      padding: toRem(44) toRem(36) toRem(36) toRem(36);
      border-radius: toRem(19);
    }
  }

  &__header {
    position: relative;
    text-align: center;
    font-weight: 600;
    font-size: toRemMob(25);
    line-height: toRemMob(29);

    @include _desktop {
      font-size: toRem(25);
      line-height: toRem(29);
    }

    &-active {
      color: $white-color;
    }
  }

  &__header {
    margin-bottom: toRemMob(30);
    @include _desktop {
      margin-bottom: toRem(41);
    }
  }

  &__form {
    margin-bottom: toRemMob(22);
    @include _desktop {
      margin-bottom: toRemMob(30);
    }
  }

  &__row {
    position: relative;

    &:not(:last-child) {
      margin-bottom: toRemMob(22);
      @include _desktop {
        margin-bottom: toRemMob(30);
      }
    }
  }

  &__error {
    position: absolute;
    bottom: toRem(-20);
    left: toRem(24);
    font-size: toRem(15);
    color: $red-color;
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

  &__close {
    position: absolute;
    right: 0;
    cursor: pointer;

    &-close {
      position: relative;
      width: toRemMob(17);
      height: toRemMob(17);

      &::before,
      &::after {
        content: "";
        position: absolute;
        left: 0;
        height: 2px;
        width: 100%;
        background-color: $white-color;
        transition: transform 0.3s ease 0s;
      }

      &::before {
        transform: rotate(45deg);
        top: 50%;
      }

      &::after {
        transform: rotate(-45deg);
        top: 50%;
      }

    }
  }
}

.modal-error {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: $body-background;
  border-radius: inherit;
  color: $white-color;

  &__image {
    width: toRemMob(50);
    height: toRemMob(50);
    margin-bottom: toRemMob(10);
    background: url("../../assets/images/modals/modal_error.svg") no-repeat center center;
    background-size: contain;
    @include _desktop {
      width: toRem(80);
      height: toRem(80);
      margin-bottom: toRem(15);
    }
  }

  &__title {
    font-size: toRemMob(30);
    @include _desktop {
      font-size: toRem(40);
    }
  }

  &__description {
    max-width: 70%;
  }

}

</style>