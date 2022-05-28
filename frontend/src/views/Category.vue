<template>
  <section class="section-category category">
    <div class="container">
      <div class="category__header">
        <h1 class="category__title page-title">{{ currentCategory.title }}</h1>
        <div @click="isOpenSortMenu = !isOpenSortMenu" class="category__sort category-sort">
          <div class="category-sort-direction">
            <svg
              @click.stop="isReverse = false"
              :class="{ active: !isReverse }"
              class="category-sort-direction__ascending"
              viewBox="0 0 16 7"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M8 0.5L15 6.5L1 6.5L8 0.5Z" stroke-linejoin="round"/>
            </svg>

            <svg
              @click.stop="isReverse = true"
              :class="{ active: isReverse }"
              class="category-sort-direction__descending"
              viewBox="0 0 16 7"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M8 0.5L15 6.5L1 6.5L8 0.5Z" stroke-linejoin="round"/>
            </svg>
          </div>
          <p class="category-sort__current">
            {{ currentSortType.title }}
          </p>
          <ul class="category-sort__list" :class="{ active: isOpenSortMenu }">
            <li
              v-for="sortType in $options.sortTypes"
              :key="sortType.value"
              @click.stop="currentSortType = sortType"
              :class="{ active: currentSortType.value === sortType.value }"
              class="category-sort__item"
            >
              {{ sortType.title }}
            </li>
          </ul>
        </div>
      </div>
      <div class="category__tasks tasks">
        <tasks-list
          v-if="sortedTasks.length"
          :tasks="sortedTasks" :current-category="currentCategory"
          :get-solved-suffix="getSolvedSuffix"
          :get-users-suffix="getUsersSuffix"
        />
        <div v-else>
          Задачу в данном направлении отсутствуют
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import TasksList from "@/components/TasksList";
import {Axios} from "@/assets/js/http-common";

export default {
  sortTypes: [
    { title: "Сортировать по алфавиту", value: "title" },
    { title: "Сортировать по дате публикации", value: "created" },
    { title: "Сортировать по очкам", value: "point_count" },
  ],

  name: "Category",
  props: {
    categories: Object,
    getSolvedSuffix: Function,
    getUsersSuffix: Function,
  },
  components: {
    TasksList,
  },
  data() {
    return {
      isOpenSortMenu: false,
      currentSortType: this.$options.sortTypes[0],
      isReverse: false,
      tasks: [],
    };
  },
  methods: {
    async getTasks() {
      try {
        const { data } = await Axios.get(`categories/${this.$route.params.categorySlug}/tasks/`);
        this.tasks = data?.tasks || [];
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    document.addEventListener("click", event => {
      if (!event.target.closest(".category-sort")) {
        this.isOpenSortMenu = false;
      }
    });
  },
  computed: {
    sortedTasks() {
      let tasks = this.tasks;
      const sortTypeValue = this.currentSortType.value || "point_count";
      if (sortTypeValue === "title") {
        tasks = tasks.sort((a, b) => a[sortTypeValue].localeCompare(b[sortTypeValue]));
      } else if (sortTypeValue === "created") {
        tasks = tasks.sort((a, b) => new Date(a[sortTypeValue]) - new Date(b[sortTypeValue]));
      } else {
        tasks = tasks.sort((a, b) => a[sortTypeValue] - b[sortTypeValue]);
      }
      return this.isReverse ? tasks.reverse() : tasks;
    },
    currentCategory() {
      this.getTasks();
      return this.categories.find((category) => category.slug === this.$route.params.categorySlug) || {};
    },
  },
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
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: start;
  }

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

@include _desktop {
  .category-sort {

    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    padding: toRem(10) toRem(50) toRem(8) toRem(50);
    margin-top: toRem(24);
    min-width: toRem(321);
    border: 1px solid $grey-color;
    border-radius: toRem(25);
    cursor: pointer;
    color: $grey-color;

    &-direction {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      height: toRem(16);
      width: toRem(14);

      &__ascending,
      &__descending {
        cursor: pointer;
        fill: $black-color;
        stroke: $grey-color;
        transition: fill 0.2s ease, stroke 0.2s ease;
        width: 16px;
        height: 7px;

        &:hover {
          fill: $grey-color-two;
        }

        &.active {
          fill: $grey-color-two;
        }
      }

      &__descending {
        transform: rotate(-180deg);
        cursor: pointer;
      }
    }

    &__list {
      position: absolute;
      top: toRem(64);
      left: 0;
      z-index: 2;
      max-width: 87%;
      min-width: toRem(267);
      width: 100%;
      padding: toRem(31) toRem(38) toRem(27) toRem(21);
      opacity: 0;
      visibility: hidden;
      background-color: $dark-grey-color;
      border-radius: toRem(19);
      color: $white-color;
      transition: opacity 0.2s ease;

      &.active {
        opacity: 1;
        visibility: visible;
      }
    }

    &__item {
      font-size: toRem(22);
      line-height: toRem(25);
      transition: color 0.2s ease;

      &:not(:first-child) {
        margin-top: toRem(34);
      }

      &.active {
        color: $grey-color-two;
      }

      &:hover {
        color: $blue-color;
      }
    }

    &__current {
      margin-left: toRem(10);
      font-size: toRem(22);
      line-height: toRem(25);
    }
  }
}

</style>
