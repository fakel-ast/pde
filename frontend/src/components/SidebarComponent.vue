<template>
  <el-aside class="sidebar">
    <el-scrollbar view-style="height: 100%">
      <el-menu
          :default-active="getActiveIndex(menu)"
          :router="true"
          :collapse="!isOpen"
          class="sidebar__menu"
          :ellipsis="true"
      >
        <el-menu-item
            v-for="itemMenu in menu"
            :key="itemMenu.id"
            :index="itemMenu.id.toString()"
            :route="itemMenu.route"
        >
          <el-icon :size="20" class="sidebar__item-icon">
            <component :is="itemMenu.icon"></component>
          </el-icon>
          <span>
            {{ itemMenu.title }}
          </span>

        </el-menu-item>
      </el-menu>
    </el-scrollbar>
  </el-aside>
</template>

<script>
import {House, Notebook, Star} from '@element-plus/icons';

export default {
  name: "SidebarComponent",
  props: {
    isOpen: Boolean,
    getActiveIndex: Function
  },
  components: {
    House, Notebook, Star
  },
  data() {
    return {
      menu: [
        {title: 'Главная', id: 1, icon: 'house', route: {name: 'Home'}},
        {title: 'Задачи', id: 2, icon: 'notebook', route: {name: 'Categories'}},
        {title: 'Рейтинг', id: 3, icon: 'star', route: {name: 'Rating'}},
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
@import "../assets/css/vars";


.sidebar {
  width: unset;

  &__menu {
    min-height: 100vh;
    height: 100%;
    &:not(.el-menu--collapse) {
      width: $sidebar-width;
    }

  }

  &__item {
    &-icon {
      margin-right: 10px;
    }
  }
}

</style>