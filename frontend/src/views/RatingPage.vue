<template>
  <section class="section-rating">
    <div class="container">
      <div class="rating__wrapper">
        <div class="rating__header rating-header">
          <ul class="rating-header__list">
            <li class="rating-header__item">Место</li>
            <li class="rating-header__item">Очки</li>
            <li class="rating-header__item">ФИО</li>
            <li class="rating-header__item">Группа</li>
          </ul>
        </div>
        <div class="rating-body">
          <ul class="rating-body__list">
            <li
              v-for="(userRating, index) in userRatings"
              :key="userRating.user_id"
              class="rating-body__item"
            >
              <p class="rating-user__text">
                <span class="rating-user__text-bold" v-if="deviceWidth.value < 640">
                  Место:
                </span>
                {{ index + 1 }}
              </p>
              <p class="rating-user__text">
                <span class="rating-user__text-bold" v-if="deviceWidth.value < 640">
                  Очки:
                </span>
                {{ userRating.points_count }}
                {{ getPointsCountSuffix(points_count) }}
              </p>
              <p class="rating-user__text">
                <span class="rating-user__text-bold" v-if="deviceWidth.value < 640">
                  ФИО:
                </span>
                {{ userRating.fio }}
              </p>
              <p class="rating-user__text">
                 <span class="rating-user__text-bold" v-if="deviceWidth.value < 640">
                  Группа:
                </span>
                {{ userRating.group_title }}
              </p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script>

import {Axios} from "../assets/js/http-common";

export default {
  name: "RatingPage",
  data() {
    return {
      userRatings: null,
    };
  },
  created() {
    this.getUserRatings();
  },
  inject: ["deviceWidth"],
  props: {
    getPointsCountSuffix: Function,
  },
  methods: {
    async getUserRatings() {
      try {
        this.userRatings = await Axios.get("user-ratings/").then(({ data }) => data.ratings || []);
      } catch (error) {
        console.error(error);
      }
    },
  },

};
</script>

<style scoped lang="scss">
.rating {
  &__wrapper {
    padding: toRem(42) toRem(45);
    background-color: $dark-grey-color;
    border-radius: toRem(20);
  }
}

.rating-header {
  display: none;
  padding-bottom: toRem(22);
  border-bottom: 1px solid $grey-color;
  @include _desktop {
    display: block;
  }
  &__list {
    display: flex;
  }

  &__item {
    width: 100%;
    @include _desktop {
      &:first-child {
        max-width: toRem(179);
      }

      &:nth-child(2) {
        max-width: toRem(233);
      }

      &:nth-child(3) {
        max-width: toRem(555);
      }

      &:nth-child(4) {
        max-width: toRem(270);
      }
    }
  }
}

.rating-body {

  @include _desktop {
    padding-top: toRem(33);
  }

  &__list {
    display: flex;
    flex-direction: column;
  }

  &__item {
    display: flex;
    flex-direction: column;
    align-items: center;

    @include _desktop {
      flex-direction: row;
    }

    &:not(:first-child) {
      margin-top: toRem(32);
    }
  }
}

.rating-user {
  &__text {
    width: 100%;
    @include _desktop {
      &:first-child {
        max-width: toRem(179);
      }

      &:nth-child(2) {
        max-width: toRem(233);
      }

      &:nth-child(3) {
        max-width: toRem(555);
      }

      &:nth-child(4) {
        max-width: toRem(270);
      }
    }

    &-bold {
      font-weight: 600;
    }


  }

}


</style>
