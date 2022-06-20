<template>
  <div class="profile-info">
    <template v-if="profile">
      <img class="profile-info__avatar" src="@/assets/images/header/kaonasi.jpg" alt="Profile image">
      <div class="profile-info__text">
        <p
          v-if="!isChangeName"
          @click="toggleChangeName"
          class="profile-info__name"
        >
          {{ profile.fio }}
        </p>
        <input
          v-else
          @blur="toggleChangeName(), updateName($event.target.value)"
          :value="profile.fio"
          class="profile-input profile-info__name"
          type="text"
          v-focus
        >
        <p
          class="profile-info__group"
        >
          Группа: {{ profile.group_title }}
        </p>
        <p class="profile-info__last">
          Последняя авторизация: {{ getAnswerDate(profile.last) }}
        </p>
        <div class="profile-info__rating">
          Рейтинг: {{ profile.rating }}
        </div>
      </div>
    </template>

  </div>
</template>

<script>
export default {
  name: "ProfileMainInfo",
  emits: {
    "update-name": null,
  },
  props: {
    profile: Object,
    getAnswerDate: Function,
  },
  data() {
    return {
      isChangeName: false,
      isChangeGroup: false,
    };
  },
  methods: {
    toggleChangeName() {
      this.isChangeName = !this.isChangeName;
    },
    updateName(newName) {
      this.$emit("update-name", newName);
    },
  },
};
</script>

<style scoped lang="scss">
.profile-info {
  background-color: $dark-grey-color;
  padding: toRemMob(39) toRemMob(32);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: toRemMob(19);
  @include _desktop {
    padding: toRem(37) toRem(47) toRem(44) toRem(47);
    flex-direction: row;
    border-radius: toRem(19);
  }

  &__avatar {
    width: toRemMob(174);
    height: toRemMob(174);
    border-radius: 50%;
    margin-bottom: toRemMob(35);

    @include _desktop {
      margin-bottom: 0;
      margin-right: toRem(66);
    }
  }

  &__text {
    display: flex;
    flex-direction: column;
    align-items: center;

    @include _desktop {
      align-items: start;
    }
  }

  &__name {
    margin-bottom: toRemMob(35);
    font-weight: 600;
    font-size: toRemMob(25);
    line-height: toRemMob(29);
    @include _desktop {
      margin-bottom: toRem(26);
    }
  }

  &__name {
    position: relative;

    &::after {
      content: "";
      top: 0;
      position: absolute;
      width: toRem(20);
      height: toRem(23);
      margin-left: toRem(9);
      background: url("../assets/images/profile/edit.svg") center center no-repeat;
      cursor: pointer;
    }
  }

  &__group {
    width: 100%;
    margin-bottom: toRemMob(15);
    @include _desktop {
      margin-bottom: toRem(17);
    }
  }

  &__last {
    width: 100%;
    margin-bottom: toRemMob(35);
    @include _desktop {
      margin-bottom: toRem(26);
    }
  }

  &__rating {
    padding: toRemMob(3) toRemMob(30) toRemMob(2) toRemMob(30);
    background-color: $blue-color;
    border-radius: toRemMob(25);
    @include _desktop {
      padding: toRem(5) toRem(30) toRem(0) toRem(30);
      border-radius: toRem(25);
    }
  }
}

.profile-input {
  border-bottom: 1px solid $body-background;
  color: $white-color;
}
</style>