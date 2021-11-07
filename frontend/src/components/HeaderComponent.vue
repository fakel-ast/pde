<template>
  <el-header class="header">
    <div class="header__sidebar-action" @click="toggleSidebar">
      <el-icon
          :class="{'reverse': isReverseSidebarIcon}"
          class="header__sidebar-icon"
      >
        <fold/>
      </el-icon>
    </div>
    <div class="header-menu">

      <el-menu
          :default-active="getActiveIndex(userMenu)"
          style="border: none"
          mode="horizontal"
          class="header-menu__list"
          :router="true"

      >
        <el-sub-menu index="1" class="header__user">
          <template #title>
            <el-avatar :size="40" class="header__user-avatar"></el-avatar>
            <span>Львов Степан</span>
          </template>

          <el-menu-item
              v-for="itemMenu in userMenu"
              :key="itemMenu.id"
              :index="itemMenu.id.toString()"
              :route="itemMenu.route"
          >
            <el-icon :size="20" class="submenu__icon">
              <component :is="itemMenu.icon"></component>
            </el-icon>
            {{ itemMenu.title }}
          </el-menu-item>

        </el-sub-menu>

      </el-menu>
    </div>
  </el-header>
</template>

<script>
import {Fold, HomeFilled, CircleClose} from '@element-plus/icons';

export default {
  name: "HeaderComponent",
  props: {
    isReverseSidebarIcon: Boolean,
    getActiveIndex: Function
  },
  components: {
    Fold, HomeFilled, CircleClose
  },
  data() {
    return {
      userMenu: [
        {title: 'Профиль', icon: 'home-filled', id: '1-1', route: {name: 'Profile'}},
        {title: 'Выйти', icon: 'circle-close', id: '1-2', route: {name: 'Logout'}},
      ],
      active: '1-1'
    }
  },
  methods: {
    toggleSidebar() {
      this.$emit('toggle-sidebar')
    }
  },
}
</script>

<style lang="scss" scoped>
@import "../assets/css/functions";

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 0.46875rem 2.1875rem rgba(4, 9, 20, 0.03), 0 0.9375rem 1.40625rem rgba(4, 9, 20, 0.03), 0 0.25rem 0.53125rem rgba(4, 9, 20, 0.05), 0 0.125rem 0.1875rem rgba(4, 9, 20, 0.03);

  &__sidebar-icon {
    font-size: toRem(30);
    cursor: pointer;

    &.reverse {
      transform: scaleX(-1);
    }
  }

  &-menu {
    width: 100%;

    &__list {
      justify-content: flex-end;
    }
  }

  &__user {
    &-avatar {
      margin-right: 20px;
    }
  }
}

</style>