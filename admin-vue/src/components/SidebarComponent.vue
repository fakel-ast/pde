<template>
  <el-aside class="sidebar">


    <el-menu
      active-text-color="#ffd04b"
      background-color="#545c64"
      class="sidebar-menu"
      :default-active="activeIndex"
      text-color="#fff"
      :collapse="isCollapse"
      :router="true"
    >
      <template
        v-for="itemMenu in filteredMenu"
        :key="itemMenu.id"
      >
        <component
          :is="itemMenu.children ? 'el-sub-menu' : 'el-menu-item'"
          :index="itemMenu.id.toString()"
          @click="$emit('change-current-item-menu', itemMenu)"
          :route="{name: itemMenu.routeName}"
        >
          <el-icon v-if="!itemMenu.children" :size="20" class="sidebar__icon">
            <div v-if="itemMenu.googleIcon" class="material-symbols-outlined">
              {{ itemMenu.googleIcon }}
            </div>
            <component v-else :is="itemMenu.icon"/>
          </el-icon>

          <template #title>
            <el-icon v-if="itemMenu.children" :size="20" class="sidebar__icon">
              <div v-if="itemMenu.googleIcon" class="material-symbols-outlined">
                {{ itemMenu.googleIcon }}
              </div>
              <component v-else :is="itemMenu.icon"/>
            </el-icon>
            <span>{{ itemMenu.title }}</span>
          </template>

          <template v-if="itemMenu.children && itemMenu.children.length">
            <el-menu-item
              v-for="itemChildrenMenu in itemMenu.children"
              @click="$emit('change-current-item-menu', itemChildrenMenu)"
              :key="itemChildrenMenu.id"
              :index="`${itemMenu.id}-${itemChildrenMenu.id}`"
              :route="{name: itemChildrenMenu.routeName}"
            >
              <el-icon :size="20" class="sidebar__icon">
                <div v-if="itemChildrenMenu.googleIcon" class="material-symbols-outlined">
                  {{ itemChildrenMenu.googleIcon }}
                </div>
                <component v-else :is="itemChildrenMenu.icon"/>
              </el-icon>
              <span>{{ itemChildrenMenu.title }}</span>
            </el-menu-item>
          </template>
        </component>


      </template>
    </el-menu>


  </el-aside>
</template>


<script>

// import {Axios} from "../http-comon";

import {Edit, Star, Coffee, House, Notebook, Plus, Coin, List, User, InfoFilled, Document} from "@element-plus/icons";

import {defineComponent, ref, computed} from "vue";
import {useRoute} from "vue-router";

export default defineComponent({
  emits: {
    "change-current-item-menu": null
  },
  props: {
    isCollapse: Boolean,
    currentUser: Object
  },
  components: {
    Edit,
    Star,
    Coffee,
    House,
    Notebook,
    Plus,
    Coin,
    List,
    User,
    InfoFilled,
    Document
  },
  setup() {
    const menu = ref([
      {
        title: "Главная",
        id: 1,
        icon: "InfoFilled",
        routeName: "home",
      },
      {
        title: "Категории задач",
        id: 2,
        googleIcon: "category",
        routeName: "Categories",
      },
      {
        title: "Задачи",
        id: 3,
        googleIcon: "task",
        routeName: "home",
      },
      {
        title: "Группы",
        id: 4,
        googleIcon: "group",
        routeName: "home",
      },
    ]);
    const route = useRoute();
    const activeIndex = computed(() => {
      for (const itemMenu of menu.value) {
        if (route.name === itemMenu.routeName) {
          return itemMenu.id.toString();
        }
        const subMenuItem = (itemMenu.children || []).find(subMenuItem => route.name === subMenuItem.routeName);
        if (subMenuItem) return `${itemMenu.id}-${subMenuItem.id}`;
      }
      return "0";
    });

    console.log(activeIndex.value);

    return {
      filteredMenu: menu,
      activeIndex
    };
  },
});
</script>

<style scoped lang="scss">

.sidebar {
  width: auto;

  &-menu {
    min-height: 100%;
    height: 100%;
    overflow: auto;
  }

  &__icon {
    vertical-align: baseline;
    margin-right: 7px;
  }
}

.el-menu:not(.el-menu--collapse) {
  width: 240px;
}


</style>
