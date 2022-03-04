<template>
  <div v-show="isOpen" @click="close" ref="modal" class="modal">
    <div @click.stop class="modal__body">
      <slot name="modal-error" v-if="isError">
        <div class="modal__error">
          <div class="modal__image modal__image_error"></div>
          <h2 class="modal__title modal__title_error">Ой!</h2>
          <p class="modal__description modal__description_error">
            Что-то пошло не так. Попробуйте повторить запрос.
          </p>
        </div>
      </slot>
      <slot name="modal-success" v-if="isSuccess"></slot>
      <div class="modal__header">
        <slot :close="close" name="modal-close">
          <div class="modal__close" @click="close"></div>
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
      this.$options.currentModalController.resolve(false);
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
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: $grey-color;
  background-color: rgba(0, 0, 0, .5);

  &__body {
    background-color: $dark-grey-color;
    border-radius: toRemMob(19);
    display: flex;
    flex-direction: column;
    justify-content: center;

    @include _desktop {
      min-width: toRem(427);
      padding: toRem(44) toRem(36) toRem(36) toRem(36);
      border-radius: toRem(19);

    }
  }

  &__header {
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
}

</style>