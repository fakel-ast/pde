<template>
  <div class="login">
    <el-form class="login__form" ref="loginForm" :model="loginForm" :rules="loginRules" label-width="200px">
      <el-form-item label="Имя пользователя" prop="username">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="loginForm.password" type="password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login">Войти</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {AxiosUsers} from "@/http-common";

export default {
  name: "LoginPage",
  emits: {
    logged: null
  },
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [
          {
            required: true,
            message: 'Это поле обязательно',
            trigger: 'blur',
          }
        ],
        password: [
          {
            required: true,
            message: 'Это поле обязательно',
            trigger: 'blur',
          }
        ],
      }
    }
  },
  methods: {
    login() {
      this.$refs.loginForm.validate(async (valid) => {
        if (valid) {
          try {
            await AxiosUsers.post(
              'login/',
              {
                username: this.loginForm.username,
                password: this.loginForm.password
              }
            );
            this.$message.success('Вы успешно авторизовались')
            this.$emit('logged')
          } catch (error) {
            if (error.response.status === 400) {
              this.$message.error(error.response.data.message)
            } else {
              this.$message.error(`Что-то пошло не так при загрузке дополнений: ${error}`)
            }
          }
        } else {
          return false
        }
      })
    },
  },
}
</script>

<style scoped lang="scss">

.login {
  height: 100vh;
  width: 700px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;

  &__form {
    width: 100%;
  }
}

</style>