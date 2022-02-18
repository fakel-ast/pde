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

a {
  text-decoration: none;
  color: $white-color;

  &:active {
    color: $blue-color;
    text-decoration: underline;
  }
}

html {
  line-height: 25px;
  font-size: 6vw;
  font-family: "TT Commons";
  @include _desktop {
    font-size: 1.15vw;
  }
}

body {
  background-color: $body-background;
  color: $white-color;
  font-weight: 600;
}

.button {
  padding: 10px 38px 8px 38px;
  border-radius: 40px;
  background: $blue-color;

  border: none;
  outline: none;
  cursor: pointer;
  color: $white-color;
  font-size: toRem(22);
  line-height: toRem(25);

  &:hover {
    background: $blue-gradient;
  }

  &:active {
    background: $sea-color;
  }

  &.disabled {
    background: $grey-color;
  }

}

</style>
