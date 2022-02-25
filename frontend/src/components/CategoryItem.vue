<template>
  <li class="category__item">
    <router-link :to="{ path: '/asdas' }">
      <div class="category__wrapper">
        <div
          :style="{
            'mask-image': `url(${category.image})`,
            '-webkit-mask-image': `url(${category.image})`,
          }"
          class="category__image"
        ></div>
        <p class="category__title">{{ category.title }}</p>
        <p class="category__tasks">{{ category.tasks_count }} задач</p>
      </div>
    </router-link>
  </li>
</template>

<script>
export default {
  name: "CategoryItem",
  props: {
    category: Object,
  },
};
</script>

<style scoped lang="scss">
.category {
  &__item {
    width: toRemMob(145);
    height: toRemMob(120);
    background-color: $dark-grey-color;
    border-radius: 8px;
    transition: .2s background-color ease;
    cursor: pointer;

    &:not(:nth-child(-n + 2)) {
      margin-top: toRemMob(17);
    }

    &:not(:nth-child(2n)) {
      margin-right: toRemMob(15);
    }

    &:hover {
      background-color: $blue-color;

      .category__image {
        background-color: $white-color;
      }
    }

    @include _desktop {
      width: toRem(313);
      min-height: toRem(259);
      &:not(:nth-child(-n + 2)) {
        margin-top: 0 !important;
      }
      &:nth-child(1n) {
        margin-right: toRemMob(21);
      }
      margin-right: toRem(21);

      &:not(:nth-child(-n + 4)) {
        margin-top: 20px !important;
      }
    }
  }

  &__wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: toRemMob(15);

    @include _desktop {
      padding: toRem(35) toRem(34);
    }
  }


  &__title {
    margin-bottom: toRemMob(4);
    font-size: toRemMob(12);
    line-height: toRemMob(14);

    @include _desktop {
      margin-bottom: toRem(8);
      font-size: toRem(25);
      line-height: toRemMob(29);
    }
  }

  &__tasks {
    font-size: toRemMob(10);
    line-height: toRemMob(12);
    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }
  }

  &__image {
    width: toRemMob(40);
    height: toRemMob(42);
    margin-bottom: toRemMob(15);
    background-color: #636276;
    transition: 0.2s background-color ease;
    mask-size: toRemMob(40) toRemMob(42);
    mask-position: center center;
    mask-repeat: no-repeat;

    @include _desktop {
      mask-size: toRemMob(83) toRemMob(89);
      width: toRemMob(83);
      height: toRemMob(89);
      margin-bottom: toRemMob(34);
    }
  }
}
</style>
