<template>
  <header-component/>
  <router-view
    :categories="categories"
    :get-solved-suffix="getSolvedSuffix"
    :get-users-suffix="getUsersSuffix"
  />
  <footer-component :categories="categories"/>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import FooterComponent from "@/components/FooterComponent";
import {Axios} from "@/assets/js/http-common";

export default {
  name: "App",
  components: {
    FooterComponent,
    HeaderComponent,
  },
  created() {
    this.getCategories();
  },
  data() {
    return {
      categories: [],
    };
  },
  methods: {
    async getCategories() {
      try {
        const { data } = await Axios.get("categories/");
        this.categories = data?.categories || [];
      } catch (error) {
        console.error(error);
      }
    },
    getSolvedSuffix(count) {
      count = (count || 0).toString();
      if (count[count.length - 1] === "1" && count.slice(count.length - 2) !== "11") return "Решил";
      return "Решило";
    },
    getUsersSuffix(count) {
      count = (count || 0).toString();
      if (count[count.length - 1] === "1" && count.slice(count.length - 2) !== "11") return "пользователь";
      else if (["2", "3", "4"].includes(count[count.length - 1]) && !["12", "13", "14"].includes(count.slice(count.length - 2))) {
        return "пользователя";
      }
      return "пользователей";
    },
  },
};
</script>

<style lang="scss">
@import "~reset-css";
@import "./assets/css/fonts";

* {
  box-sizing: border-box;
}

a {
  text-decoration: none;
  color: $white-color;
}


.link {
  transition: color .2s ease;

  &:active {
    color: $blue-color;
    text-decoration: underline;
  }

  &:hover {
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
    max-width: toRem(1350);
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

  &.button-red {
    transition: background-color .2s ease;

    background-color: $red-color;

    &:hover {
      background: #fe3a3a;
    }

    &:active {
      background: $red-color;
    }
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
    margin-bottom: toRem(76.771);
  }
}

.only-desktop {
  @include _mobile {
    display: none;
  }
}

.only-mobile {
  @include _desktop {
    display: none;
  }
}

.success-text {
  color: $green-color;
}

.error-text {
  color: $red-color;
}
</style>
