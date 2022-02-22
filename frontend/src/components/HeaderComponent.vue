<template>
  <header class="header">
    <div class="header__logo logo">
      <img class="logo__image" src="../assets/images/header/logo.svg" alt="CodeSkill logo"/>
      <p class="logo__text">CodeSkill</p>
    </div>
    <nav class="header__nav">
      <ul class="header__list">
        <li class="header__item">
          <a class="header__link" href="#">Задачи</a>
        </li>
        <li class="header__item">
          <a class="header__link" href="#">Рейтинг</a>
        </li>
      </ul>
    </nav>
    <div class="header__profile header-profile">
      <button class="header-profile__button button">Войти/Регистрация</button>
    </div>
    <div
      @click="isOpenMenu = !isOpenMenu"
      :class="{ active: isOpenMenu }"
      class="header__burger"
    >
      <span></span>
    </div>
    <nav class="header__menu menu" :class="{ active: isOpenMenu }">
      <ul class="menu__list">
        <li class="menu__item">Профиль</li>
        <li class="menu__item">Задачи</li>
        <li class="menu__item">Выйти из аккаунта</li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
  data() {
    return {
      isOpenMenu: false,
    };
  },
};
</script>

<style scoped lang="scss">

.header {
  display: flex;
  margin: toRemMob(22) toRemMob(28);
  @include _desktop {
    margin: toRem(50) toRem(60);
  }

  &__logo {
    display: flex;
    align-items: center;
    justify-content: space-between;
    @include _desktop {
      padding-right: toRem(40);
      border-right: 1px solid $grey-color;
    }
  }

  &__nav {
    display: none;

    @include _desktop {
      display: flex;
      margin-left: toRem(40);
    }
  }

  &__list {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__item {
    font-size: toRem(22);
    line-height: toRem(25);

    &:not(:first-child) {
      margin-left: toRem(70);
    }
  }

  &__link {
    cursor: pointer;
    transition: color 0.2s ease;

    &:hover {
      color: $blue-color;
    }
  }

  &__profile {
    display: none;
    margin-left: auto;

    @include _desktop {
      display: block;
    }
  }

  &__burger {
    position: relative;
    width: toRemMob(20);
    height: toRemMob(15);
    margin-left: auto;
    cursor: pointer;
    z-index: 2;

    @include _desktop {
      display: none;
    }

    &.active {
      &::before {
        transform: rotate(45deg);
        top: 50%;
      }

      &::after {
        transform: rotate(-45deg);
        top: 50%;
      }

      & > span {
        display: none;
      }
    }

    & > span {
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      height: 2px;
      width: 100%;
      background-color: $white-color;
    }

    &::before,
    &::after {
      content: "";
      position: absolute;
      left: 0;
      height: 2px;
      width: 100%;
      background-color: $white-color;
      transition: transform 0.3s ease 0s;
    }

    &::before {
      top: 0;
    }

    &::after {
      bottom: 0;
    }
  }

  &__menu {
    display: none;

    &.active {
      display: block;
    }
  }
}

.logo {
  &__image {
    width: toRemMob(32);
    height: toRemMob(35);

    @include _desktop {
      width: toRem(48);
      height: toRem(56);
    }
  }

  &__text {
    margin-left: toRemMob(16);
    font-size: toRemMob(21);
    line-height: toRemMob(24);
    @include _desktop {
      margin-left: toRem(23);
      font-size: toRem(33);
      line-height: toRem(38);
    }
  }
}

.menu {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;

  &__list {
    padding: toRemMob(160) toRemMob(28) 0 toRemMob(28);
  }

  &__item {
    margin-bottom: 49px;
    font-weight: 400;
  }
}
</style>
