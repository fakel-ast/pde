<template>
  <el-dropdown
    placement="bottom-end"
    trigger="click"
  >
        <span class="el-dropdown-link">
          <div class="header__user-profile">
      <div class="header__user-avatar">
        <img src="https://greendi.com/media/avatars/default.jpg" alt="Аватар">
      </div>
      <div class="header__user-info">
        <h2 class="header__user-name">
          {{ currentUser.full_name }}
        </h2>
        <small class="header__user-group">
          {{ currentUser.position }}
        </small>
      </div>
    </div>
        </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item
          class="header__user-menu-element">
          <span class="material-symbols-outlined">exit_to_app</span>
          Выйти
        </el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script>
export default {
  name: "Profile",
  emits: {
    "is-user-auth": null,
  },
  props: {
    currentUser: Object
  },
  data() {
    return {
      isUserAuth: true
    }
  }
}
</script>

<style scoped lang="scss">
.header__user {
  &-profile {
    display: flex;
    align-items: center;
    font-size: 1rem;
    height: 60px;
    cursor: pointer;
    padding: 0 15px;
    transition: all .2s ease-in;

    &:hover {
      background: #e7e7e7;
    }
  }

  &-avatar {
    margin-right: .5rem;

    img {
      width: 50px;
      height: 50px;
      border-radius: 50%;
    }
  }

  &-group {
    font-size: .8rem;
    color: #707070;
  }

  &-name {
    overflow-wrap: break-word;
    max-width: 15rem;
  }

  &-menu-element {
    display: flex;
    align-items: center;

    span {
      font-size: 1.3rem;
      margin-right: .2rem;
    }
  }
}


.el-dropdown {
  vertical-align: top;
}

.el-dropdown + .el-dropdown {
  margin-left: 15px;
}

.el-icon-arrow-down {
  font-size: 12px;
}
</style>