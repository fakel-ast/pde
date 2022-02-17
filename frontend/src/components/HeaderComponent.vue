<template>
  <header class="header">
    <div class="header__logo logo">
      <img class="logo__image" src="../assets/images/header/logo.svg" alt="CodeSkill logo"/>
      <p class="logo__text">CodeSkill</p>

    </div>
    <nav class="header__nav">
      <ul class="header__list">
        <li class="header__item">Задачи</li>
        <li class="header__item">Рейтинг</li>
      </ul>
    </nav>
    <div class="header__profile header-profile">
      <button class="header-profile__button button button-blue">Войти/Регистрация</button>
    </div>
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  align-items: center;
  margin: toRem(50) toRem(60);
  padding: toRem(15) 0;

  &__logo {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-right: toRem(40);
    border-right: 1px solid #3A3762;
  }

  &__nav {
    margin-left: toRem(40);

  }

  &__list {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__item {
    &:not(:first-child) {
      margin-left: toRem(70);
    }
  }
}

.logo {
  &__image {
    width: toRem(48);
    height: toRem(56);
  }

  &__text {
    margin-left: toRem(23);
    font-size: toRem(33);
  }
}
</style>