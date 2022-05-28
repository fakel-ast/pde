<template>
  <section class="section-footer">
    <div class="container">
      <footer class="footer">
        <div class="footer__item footer-item">
          <div class="footer-item__title">
            Меню
          </div>
          <nav class="footer-nav footer-nav">
            <ul class="footer-nav__list">
              <li class="footer-nav__item">
                <router-link class="footer-nav__link footer-link" :to="{name: 'Categories'}">Задачи</router-link>
              </li>
              <li class="footer-nav__item">
                <router-link class="footer-nav__link footer-link" :to="{name: 'RatingPage'}">Рейтинг</router-link>
              </li>
              <li class="footer-nav__item" @click="openModalLogin">
                <p class="footer-nav__link footer-link" >
                  Вход/Регистрация
                </p>
              </li>
            </ul>
          </nav>
        </div>
        <div class="footer__item">
          <div class="footer-item__title footer-item__title_margin">
            Направления
          </div>
          <div class="footer-directions">
            <ul class="footer-directions__list">
              <li
                v-for="category in categories"
                :key="`catgory-${category.id}`"
                class="footer-directions__item"
              >
                <router-link class="footer-link" :to="{ name: 'Category', params: { categorySlug: category.slug } }">
                  {{ category.title }}
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </footer>
    </div>
  </section>

</template>

<script>
export default {
  name: "FooterComponent",
  props: {
    categories: Array,
    openModalLogin: Function,
  },
};
</script>

<style scoped lang="scss">
.section-footer {
  padding-top: toRemMob(50);
  @include _desktop {
    padding-top: toRem(108);
  }
}

.footer {
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  padding-bottom: toRemMob(10);

  @include _desktop {
    flex-direction: row;
    padding-bottom: toRem(15);
  }

  &__item {
    @include _desktop {
      &:first-child {
        width: 15%;
      }

      &:last-child {
        width: 75%;
      }
    }
  }

  &-item {
    &__title {
      margin-bottom: toRemMob(40);
      padding-bottom: toRemMob(20);
      font-weight: 600;
      font-size: toRemMob(25);
      line-height: toRemMob(29);
      border-bottom: 1px solid $grey-color;
      @include _desktop {
        padding-bottom: toRem(20);
        margin-bottom: toRem(40);
        font-size: toRem(25);
        line-height: toRem(29);
      }

      &_margin {
        margin-top: toRemMob(40);
        @include _desktop {
          margin-top: 0;
        }
      }
    }
  }

  &-link {
    transition: color .2s ease;

    &:hover {
      color: $blue-color;
    }
  }
}

.footer-nav {
  &__list {
    display: flex;
    flex-direction: column;
  }

  &__item {
    font-size: toRemMob(19.2);
    line-height: toRemMob(22);

    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }

    &:not(:first-child) {
      margin-top: toRemMob(26);
      @include _desktop {
        margin-top: toRem(30);
      }
    }
  }
}

.footer-directions {
  &__list {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    @include _desktop {
      max-height: toRem(192);
    }

  }

  &__item {
    &:not(:first-child) {
      margin-top: toRemMob(26);
    }

    @include _desktop {
      &:nth-child(1n) {
        margin-top: 0;
      }
      &:not(:nth-child(4n+1)) {
        margin-top: toRem(31);
      }
    }
  }
}

.design-author {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: toRemMob(175);
  margin: 0 auto;
  padding: toRem(40) 0 toRem(35) 0;
  @include _desktop {
    max-width: toRem(240);
    padding: toRem(67) 0 toRem(40) 0;
  }

  &__img {
    width: toRemMob(22);
    height: toRemMob(25);
    @include _desktop {
      width: toRem(29);
      height: toRem(34);
    }
  }

  &__text {
    font-size: toRemMob(16.0591);
    line-height: toRemMob(18);
    color: $grey-color;
    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }
  }
}

.footer-link {
  cursor: pointer;
}
</style>