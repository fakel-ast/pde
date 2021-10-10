<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/tasks">Tasks</router-link> |
    <router-link to="/sign-up">Sign up</router-link> |
  </div>
  <router-view/>
</template>

<style lang="scss">
@import "../public/css/reset.css";

.el-container {
  max-width: 1400px;
  margin: 0 auto;
}
</style>
