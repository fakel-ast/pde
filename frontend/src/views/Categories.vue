<template>
  <section class="section-categories">
    <div class="container">
      <h1 class="page-title">
        Направления
      </h1>
      <ul class="category__list">
        <category-item
          v-for="category in categories"
          :key="category.id"
          :category="category"
        />
      </ul>
    </div>
  </section>

</template>

<script>
import CategoryItem from "@/components/CategoryItem";

export default {
  name: "Categories",
  components: {
    CategoryItem
  },
  data() {
    return {
      categories: [
        {id: 1, title: "Администрирование", image: require("../assets/images/categories/admin.svg"), tasks_count: 91},
        {id: 2, title: "Криптография", image: require("../assets/images/categories/admin.svg"), tasks_count: 9},
        {id: 3, title: "Развлечения", image: require("../assets/images/categories/admin.svg"), tasks_count: 2},
        {id: 4, title: "Криминалистика", image: require("../assets/images/categories/admin.svg"), tasks_count: 9},
        {id: 5, title: "Хеши", image: require("../assets/images/categories/admin.svg"), tasks_count: 0},
        {id: 6, title: "Сети", image: require("../assets/images/categories/admin.svg"), tasks_count: 9},
        {id: 7, title: "Развлечения", image: require("../assets/images/categories/admin.svg"), tasks_count: 9},
        {id: 8, title: "Криминалистика", image: require("../assets/images/categories/admin.svg"), tasks_count: 12},
        {id: 9, title: "Криптография", image: require("../assets/images/categories/admin.svg"), tasks_count: 15},
        {id: 10, title: "Криптография", image: require("../assets/images/categories/admin.svg"), tasks_count: 9},
        {id: 11, title: "Развлечения", image: require("../assets/images/categories/admin.svg"), tasks_count: 13},
      ]
    };
  }
};
</script>

<style scoped lang="scss">
.section-categories {
  padding-top: toRemMob(21);
  @include _desktop {
    padding-top: toRem(59);
  }
}
.category {
  &__list {
    display: flex;
    flex-wrap: wrap;
  }
}
</style>