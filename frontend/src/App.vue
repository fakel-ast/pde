<template>
  <header-component/>
  <router-view :categories="categories"/>
  <footer-component :categories="categories"/>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";

export default {
  name: "App",
  components: {
    FooterComponent,
    HeaderComponent,
  },
  data() {
    return {
      categories: [
        {id: 1, title: "Администрирование", image: require("./assets/images/categories/admin.svg"), tasks_count: 91},
        {id: 2, title: "Криптография", image: require("./assets/images/categories/crypto.svg"), tasks_count: 9},
        {id: 3, title: "Развлечения", image: require("./assets/images/categories/entertainment.svg"), tasks_count: 2},
        {
          id: 4,
          title: "Криминалистика",
          image: require("./assets/images/categories/criminalistics.svg"),
          tasks_count: 9
        },
        {id: 5, title: "Хеши", image: require("./assets/images/categories/hesh.svg"), tasks_count: 0},
        {id: 6, title: "Сети", image: require("./assets/images/categories/networks.svg"), tasks_count: 9},
        {
          id: 7,
          title: "Программирование",
          image: require("./assets/images/categories/programming.svg"),
          tasks_count: 9
        },
        {id: 8, title: "Разведка", image: require("./assets/images/categories/exploration.svg"), tasks_count: 12},
        {id: 9, title: "Бинарный код", image: require("./assets/images/categories/bin_code.svg"), tasks_count: 15},
        {id: 10, title: "Стенография", image: require("./assets/images/categories/databse.svg"), tasks_count: 9},
        {id: 11, title: "Квесты", image: require("./assets/images/categories/quests.svg"), tasks_count: 13},
        {id: 12, title: "Веб", image: require("./assets/images/categories/web.svg"), tasks_count: 13},
      ]
    };
  }
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
  @include _max {
    font-size: 22.57px;
  }
}

body {
  background-color: $body-background;
  color: $white-color;
  font-weight: normal;
}

.container {
  padding: 0 toRemMob(28);
  margin: 0 auto;

  @include _desktop {
    padding: 0 toRem(15);
    max-width: toRem(1320);
  }
}

.button {
  padding: toRem(10) toRem(37) toRem(8) toRem(37);
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

.page-title {
  font-size: toRemMob(25);
  line-height: toRemMob(29);
  margin-bottom: toRemMob(25);
  font-weight: 600;

  @include _desktop {
    font-size: toRem(86);
    line-height: toRemMob(99);
    margin-bottom: toRem(70);
  }
}

</style>
