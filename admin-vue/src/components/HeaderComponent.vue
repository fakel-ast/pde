<template>
  <el-header class="header">
    <el-icon
      class="header__open-icon"
      @click="$emit('toggle-header')"
    >
      <my-menu/>
    </el-icon>
    <div class="header__content">
      <div @click="clickEvent" class="header__logo"></div>
      <profile-menu
        :current-user="currentUser"
        @is-user-auth="$emit('auth-switch', $event)"
      />
    </div>

  </el-header>
</template>

<script>
import {Menu as myMenu} from "@element-plus/icons";
import ProfileMenu from "./ProfileMenu";

export default {
  name: "Header",
  emits: {"auth-switch": null, "toggle-header": null, "easter-egg": null},
  components: {
    myMenu,
    ProfileMenu
  },
  props: {
    currentUser: Object
  },
  data() {
    return {
      clickCounter: 0,
      timeStart: null
    };
  },
  methods: {
    clickEvent() {
      this.timeStart = new Date().getTime();
      this.clickCounter += 1;
      setTimeout(() => {
        if (this.timeStart && this.timeStart <= new Date().getTime() - 600) {
          if (this.clickCounter === 11) {
            this.$emit("easter-egg");
          }
          this.clickCounter = 0;
        }
      }, 600);
    }
  }
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  align-items: center;
  background: #fafbfc;
  box-shadow: 0 0.46875rem 2.1875rem rgba(4, 9, 20, 0.03), 0 0.9375rem 1.40625rem rgba(4, 9, 20, 0.03), 0 0.25rem 0.53125rem rgba(4, 9, 20, 0.05), 0 0.125rem 0.1875rem rgba(4, 9, 20, 0.03);

  &__logo {
    width: 120px;
    height: 40px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    cursor: pointer;
    background-image: url("../assets/images/icons/logo.svg");
  }

  &__open-icon {
    font-size: 36px;
    cursor: pointer;
  }

  &__content {
    display: flex;
    align-items: inherit;
    width: 100%;
    margin-left: 20px;
    justify-content: space-between;
  }

  &__title {
    font-size: var(--el-font-size-extra-large);

  }

  &__user {
    display: flex;

    &-avatar {
      margin-right: 20px;
    }

    &-info {
      display: flex;
      justify-content: center;
      flex-direction: column;
    }

    &-group {
      font-size: var(--el-font-size-small);
    }
  }
}
</style>