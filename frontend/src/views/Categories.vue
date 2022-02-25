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
  props: {
    categories: Array,
  },
  components: {
    CategoryItem
  },
  data() {
    return {};
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
    @include _desktop {
      margin-right: -0.93044rem;
    }
  }
}
</style>