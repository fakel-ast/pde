<template>
  <header-component/>
  <router-view/>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";

export default {
  name: "App",
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss">
@import "~reset-css";
@import "./assets/css/fonts";

html {
  font-size: 16px;

}

body {
  background-color: $body-background;
  color: $white-color;
  font-weight: 600;
}
</style>
