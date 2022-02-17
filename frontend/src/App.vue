<template>
  <header-component />
  <router-view />
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

</style>
