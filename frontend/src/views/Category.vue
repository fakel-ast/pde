<template>
  <section class="section-category category">
    <div class="container">
      <div class="category__header">
        <h1 class="category__title page-title">Администрирование</h1>
        <div class="category__sort category-sort"></div>
      </div>
      <div class="category__tasks tasks">
        <tasks-list :tasks="tasks"/>
      </div>
    </div>

  </section>
</template>

<script>
import TasksList from "@/components/TasksList";

export default {
  name: "Category",
  components: {
    TasksList
  },
  data() {
    return {
      tasks: [
        {id: 1, slug: "1", title: "Журналы", point_count: 216, is_solved: true, solved_count: 1},
        {id: 2, slug: "2", title: "Cron", point_count: 268, is_solved: false, solved_count: 1011},
        {id: 3, slug: "3", title: "Test", point_count: 164, is_solved: false, solved_count: 1002},
        {id: 4, slug: "4", title: "Git", point_count: 245, is_solved: false, solved_count: 13},
        {id: 5, slug: "5", title: "Repo", point_count: 224, is_solved: true, solved_count: 14},
        {id: 6, slug: "6", title: "Admin_vol1", point_count: 230, is_solved: false, solved_count: 17},
        {id: 7, slug: "7", title: "Docker", point_count: 281, is_solved: false, solved_count: 0},
        {id: 8, slug: "8", title: "Image", point_count: 291, is_solved: false, solved_count: 0},
        {id: 9, slug: "9", title: "Shiver PC", point_count: 268, is_solved: true, solved_count: 11},
        {id: 10, slug: "10", title: "Журналы", point_count: 192, is_solved: false, solved_count: 2},
        {id: 11, slug: "11", title: "Cron", point_count: 133, is_solved: false, solved_count: 1},
        {id: 12, slug: "12", title: "Test", point_count: 150, is_solved: false, solved_count: 7},
      ]
    };
  }
};
</script>

<style scoped lang="scss">

.section-category {
  padding-top: toRemMob(20);
  @include _desktop {
    padding-top: toRem(59);
  }
}

.category {
  &__sort {
    display: none;
    @include _desktop {
      display: block;
    }
  }

  &__title {
    @include _desktop {
      margin-bottom: toRem(81.285);
    }
  }
}

</style>