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

        <el-form-item label="Имя пользователя" prop="username">
          <el-input v-model="signInForm.username"></el-input>
        </el-form-item>

        <el-form-item label="Пароль" prop="password">
          <el-input type="password" v-model="signInForm.password" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button @click="submitForm('signInForm')" type="primary">Войти</el-button>
          <el-button @click="resetForm('signInForm')">Сбросить</el-button>
        </el-form-item>

      </el-form>
    </el-main>
  </el-container>
</template>

<script>
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
          {required: true, min: 5, max: 12, message: 'Длина должна быть от 5 до 12 символов', trigger: 'blur'},
          {validator: this.validatePassword, trigger: 'blur'},
        ]
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
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
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