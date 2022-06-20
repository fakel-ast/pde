<template>
  <section class="section-profile profile">
    <div class="container">
      <h1 class="page-title">
        Профиль
      </h1>
      <div class="profile__header">
        <profile-main-info
          v-if="page === 'profile'"
          @update-name="updateProfileName"
          :profile="profile"
          :get-answer-date="getAnswerDate"
          class="profile__main-info"
        />
        <profile-security
          v-if="page === 'security'"
          :profile="profile"
          class="profile__security"
        >
        </profile-security>
        <div class="profile__nav profile-nav">
          <ul class="profile-nav__list">
            <li
              @click="page = 'profile'"
              :class="{disabled: page === 'profile'}"
              class="profile-nav__item button"
            >
              Профиль
            </li>
            <!--            <li-->
            <!--              @click="page = 'security'"-->
            <!--              :class="{disabled: page === 'security'}"-->
            <!--              class="profile-nav__item button"-->
            <!--            >-->
            <!--              Безопасность-->
            <!--            </li>-->
            <li class="profile-nav__item button button-red" @click="logout(), redirectToMainPage()">
              Выйти
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import ProfileMainInfo from "@/components/ProfileMainInfo";
import ProfileSecurity from "@/components/ProfileSecurity";
import {Axios} from "@/assets/js/http-common";

export default {
  name: "Profile",
  props: {
    getAnswerDate: Function,
    logout: Function,
  },
  components: {
    ProfileMainInfo,
    ProfileSecurity,
  },
  created() {
    this.getProfile();
  },
  data() {
    return {
      profile: null,
      page: "profile",
    };
  },
  methods: {
    async getProfile() {
      const data = await Axios.get("profile/").then(({ data }) => data);
      this.profile = data.profile;
      this.profile.rating = data.rating;
    },
    async updateProfile() {
      await Axios.post("profile/", this.profile);
    },
    updateProfileName(newName) {
      this.profile.fio = newName;
      this.updateProfile();
    },
    updateProfileGroup(newGroup) {
      this.profile.group = newGroup;
      this.updateProfile();
    },
    redirectToMainPage() {
      this.$router.push({ name: "Categories" });
    },
  },
};
</script>

<style scoped lang="scss">
.profile {
  &__header {
    display: flex;
    flex-direction: column;
    align-items: center;
    @include _desktop {
      flex-direction: row;
      justify-content: space-between;
      align-items: start;
    }
  }

  &__main-info {
    margin-bottom: toRemMob(20);
    @include _desktop {
      width: 100%;
      margin-bottom: 0;
      margin-right: toRem(130);
    }
  }

  &__nav {
    width: 100%;
    @include _desktop {
      max-width: toRem(315);
    }
  }
}

.profile-nav {
  &__list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  &__item {
    width: 100%;
    text-align: center;

    &:not(:last-child) {
      margin-bottom: toRemMob(20);
      @include _desktop {
        margin-bottom: toRem(20);
      }
    }

  }
}
</style>
