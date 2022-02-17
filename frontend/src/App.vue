<template>
  <!-- Header start-->
  <header-component
      @toggle-sidebar="isOpenSidebar = !isOpenSidebar"
      :is-reverse-sidebar-icon="!isOpenSidebar"
      :get-active-index="getActiveIndex"
  />
  <!-- header end -->
  <el-container direction="vertical" v-loading="false" element-loading-text="Загрузка..."
                element-loading-background="rgba(0, 0, 0, 0.8)"
                element-loading-spinner="el-icon-loading" class="container">

    <router-view/>
  </el-container>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent";

export default {
  name: "App",
  data() {
    return {
      isOpenSidebar: true
    }
  },
  components: {
    HeaderComponent
  },
  methods: {
    getActiveIndex(menuArray) {
      return (menuArray.find(itemMenu => itemMenu.route.name === this.$route.name)?.id || '').toString()
    }
  }
}

</script>

<style lang="scss">
@import "../public/css/reset.css";

#app {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
  'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
}

.el-sub-menu__title:hover {
  background-color: unset;
}

.el-menu-item {
  display: flex;
  align-items: center;
}

.el-menu-item:hover {
  background-color: #F2F6FC !important;
}

.el-menu-item * {
  vertical-align: unset;
}

.submenu__icon {
  margin-right: 10px;
}

</style>
