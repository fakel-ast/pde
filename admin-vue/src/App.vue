<template>
  <template v-if="easterEggShow">
    <greendi-bird></greendi-bird>
  </template>
  <template v-else>
      <template v-if="!isLoadUserInfo">
    <el-container class="is-vertical" v-if="isUserAuth">
      <header-component
        class="header"
        :current-user="currentUser"
        @toggle-header="toggleHeader"
        @auth-switch="toggleUserAuth"
        @easter-egg="easterEgg"
      />
      <el-container class="content">
        <sidebar-component
          @change-current-item-menu="changeCurrentItemMenu"
          :isCollapse="isCollapse"
          :current-user="currentUser"
        />
        <el-main>
          <router-view
            :get-span="getSpan"
            :nice-price="nicePrice"
            :get-language-object="getLanguageObject"
            :get-image="getImage"
            :default-language="defaultLanguage"
            :upload-image="uploadImage"
          />
        </el-main>
      </el-container>
    </el-container>
    <el-container v-else>
      <login-page @logged="loggedUser"/>
    </el-container>
  </template>
  </template>
</template>
<script>
import SidebarComponent from "./components/SidebarComponent";
import LoginPage from "./views/LoginPage";
import HeaderComponent from "./components/HeaderComponent";
import GreendiBird from "@/easter_egg/GreendiBird";

import {AxiosApi} from "@/http-common";

export default {
  name: "Admin",
  data() {
    return {
      isCollapse: false,
      currentItemMenu: {},
      currentUser: {},
      isUserAuth: false,
      isLoadUserInfo: true,
      defaultLanguage: "ru",
      easterEggShow: false
    };
  },
  components: {
    SidebarComponent,
    HeaderComponent,
    GreendiBird,
    LoginPage
  },
  emits: ["auth-switch"],
  created() {
    this.checkLogin();
  },
  provide() {
    return {
      replaceHTML: this.replaceHTML
    };
  },
  methods: {
    toggleUserAuth(event) {
      this.isUserAuth = event;
    },
    toggleHeader() {
      this.isCollapse = !this.isCollapse;
    },
    changeCurrentItemMenu(newItemMenu) {
      this.currentItemMenu = newItemMenu;
    },
    getSpan(count) {
      return Math.ceil(24 / count);
    },
    async checkLogin() {
      try {
        const response = await AxiosApi.get("users/current/");
        this.isUserAuth = response.status === 200 && !response.data.errors;
        this.currentUser = response?.data.user;
        this.isLoadUserInfo = false;
      } catch (error) {
        this.isUserAuth = false;
        this.isLoadUserInfo = false;
      }
    },
    loggedUser() {
      this.isUserAuth = true;
    },
    nicePrice(price) {
      return new Intl.NumberFormat("ru").format(price);
    },
    getLanguageObject(object, needFields) {
      const newObject = {};
      let newObjectFields = {};
      try {
        needFields.forEach(field => {
          Object.keys(object[field]).forEach(language => Object.assign(newObjectFields, {[language]: null}));
          newObject[field] = newObjectFields;
          newObjectFields = {};
        });
        return newObject;
      } catch (error) {
        console.error(error);
        return {};
      }
    },
    replaceHTML(rawValue) {
      if (rawValue && rawValue.length) {
        return rawValue.replace(/<.*?>/g, "");
      }
    },
    getImage(objectWithImage, imageField = "image", filePath = this.$host) {
      if (objectWithImage[imageField] === null) return null;
      if (typeof objectWithImage[imageField] === "object") {
        return objectWithImage[imageField].base_64;
      } else {
        return filePath + objectWithImage[imageField];
      }
    },
    uploadImage(uploadData) {
      const {file, element, fieldName} = uploadData;
      element[fieldName] = {filename: file.name};
      const reader = new FileReader();
      reader.onloadend = () => {
        element[fieldName].base_64 = reader.result;
      };
      reader.readAsDataURL(file);
    },
    easterEgg() {
      this.easterEggShow = true;
    }
  }
};
</script>

<style lang="scss">
@import '/node_modules/reset-css';
@import url(assets/fonts/font.css);


body {
  font-family: Roboto;
}

.header {
  position: fixed;
  width: 100%;
  z-index: 1;
}

.content {
  padding-top: 60px;
}

.body {
  &_admin {
    //overflow: hidden;
  }
}

main {
  //overflow: hidden !important;
  height: calc(100vh - 60px);
}

* {
  box-sizing: border-box;
}

input {
  outline: none;
}

.button {
  &_full-width {
    width: 100%;
  }
}


.el-main {
  &__table-price {
    margin-bottom: 30px;
  }
}

//:not(.el-select-dropdown) > .el-scrollbar > .el-scrollbar__wrap {
//  height: 100vh !important;
//}

.el-scrollbar {
  height: unset !important;
}

.greenhouse-card {

  .el-menu {
    border: none;

    &-item {
      height: 36px;
      line-height: 35px;
    }
  }

  &:not(:last-child) {
    margin-bottom: 20px;
  }


  &__title {
    padding-left: 20px;
    font-weight: 600;
    font-size: 18px;
  }
}

.item {

  &_table {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #D3D3D3;
    font-weight: 400;
    color: #1D1D1D;
    font-size: 18px;
    line-height: 24px;
    border-bottom: 1px solid #D3D3D3;

    &:last-child {
      border-bottom: unset;
    }

    &:first-child {
      > div {
        align-items: flex-start;
        height: 64px;
        padding-top: 10px;
        font-weight: 300;
        line-height: 18px;
      }
    }

    > div {
      display: flex;
      align-items: center;
      justify-content: space-around;
      min-width: 165px;
      max-width: 165px;
      height: 53px;
      border-right: 1px solid #D3D3D3;

      &:first-child {
        justify-content: flex-start;
        min-width: 95px;
        max-width: 95px;
        font-weight: 300;
      }

      &:last-child {
        border-right: unset;
      }
    }

  }

  &__table-price {
    position: relative;
    padding: 10px 12px;
    border: 1px solid transparent;
    border-radius: 2px;
    transition: all .2s ease;
    cursor: pointer;
    white-space: nowrap;

    &:before {
      content: '';
      position: absolute;
      width: 0;
      height: 0;
      left: 3px;
      top: 5px;
      background-color: #3CB156;
      border-radius: 50%;
      transition: all .2s ease;

    }

    &.active {
      border: 1px solid #21A73F;
    }

    &.buy {
      &:before {
        width: 8px;
        height: 8px;
      }
    }

    &:hover {

      border: 1px solid #21A73F;
    }

    &:active {

      background: rgba(33, 167, 63, 0.1);
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    }

    span {

      display: inline-flex;
    }
  }

  &__table-input {
    display: block;
    padding: 10px 0;
    width: 100%;
    margin: 0 20px;
    border: none;
    text-align: center;

  }

  &__table-input-discount {
    display: block;
    padding: 10px 0;
    width: 100%;
    margin: 0 20px;
    border: none;
    text-align: center;
    background-color: #F56C6C;
    color: #FFFFFF;
  }

  &__table-title {
    width: 130px;
  }
}

.buttons-wrapper {
  display: flex;
  align-items: center;
  margin: 20px 0 0 0;

  &.buttons-end {
    justify-content: flex-end;
  }
}

.buttons {
  &__delete {
    color: #F56C6C;
    cursor: pointer;
  }

  &__add-conf {
    width: 100%;
    margin: 20px auto;
  }
}

.add-conf-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 19px;
}

.configuration-select {
  width: 100%;
  margin: 20px 0 0 0;
}

.small-text {
  font-size: 13px;
}

.red-text {
  color: red;
}


.hint {
  &__content {
    padding: 20px;
  }
}

.el-form-item {
  align-items: center;
}

.hint-image {
  min-width: 294px;
  min-height: 166px;

  img {
    display: block;
  }
}

.el-scrollbar {
  .el-scrollbar__bar.is-horizontal {
    height: 0px;
    left: 0px;
  }
}

.handle {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  cursor: move;

  &__line {
    border-radius: 2px;
    width: 19px;
    height: 3px;
    background-color: #8a8a8a;
    margin: 1px 0;
  }
}


</style>
