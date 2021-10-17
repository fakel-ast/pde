<template>
  <el-container class="sign-in-container">
    <el-main>
      <el-form
          :model="signInForm"
          :rules="rules"
          status-icon
          ref="signInForm"
          label-width="165px"
          class="sign-in-form form"
      >

        <el-form-item label="Имя пользователя" prop="username" :error="modelErrors.username">
          <el-input v-model="signInForm.username" placeholder="Имя пользователя"></el-input>
        </el-form-item>

        <el-form-item label="Пароль" prop="password" :error="modelErrors.password">
          <el-input type="password" v-model="signInForm.password" autocomplete="off" placeholder="Пароль"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button @click="submitForm('signInForm')" type="primary">Войти</el-button>
        </el-form-item>

      </el-form>
    </el-main>
  </el-container>
</template>

<script>
import { Axios } from "@/http-common";

export default {
  name: "SingUp",
  data() {
    return {
      signInForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          {required: true, message: 'Пожалуйста, введите имя пользователя', trigger: 'blur'},
        ],
        password: [
          {required: true, min: 8, message: 'Минимальная длина пароля 8 символов', trigger: 'blur'},
          {validator: this.validatePassword, trigger: 'blur'},
        ]
      },
      modelErrors: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    validatePassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('Пожалуйста, введите пароль'));
      } else {
        if (this.signInForm.password2 !== '') {
          this.$refs.signInForm.validateField('password2');
        }
        callback();
      }
    },
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          const {errors, data} = await this.$sendForm('users/sign-in/', this.signInForm, 'post', this.modelErrors)
          if (!errors) {
            this.$message.success(`Вы успешно вошли как ${data.username}`)
          } else {
            this.modelErrors = {}
            setTimeout(() => {
              this.modelErrors = data.modelErrors
            }, 200)
          }
        } else {
          return false;
        }
      });

    }
  }
}
</script>

<style scoped lang="scss">
.sign-in-form {
  max-width: 700px;
  margin: 0 auto;
}

.sign-in-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>