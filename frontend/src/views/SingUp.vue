<template>
  <el-container class="sign-up-container">
    <el-main>
      <el-form
          :model="signUpForm"
          :rules="rules"
          status-icon
          ref="signUpForm"
          label-width="165px"
          class="sign-up-form form"
      >

        <el-form-item label="Имя пользователя" prop="username" :error="modelErrors.username">
          <el-input v-model="signUpForm.username"></el-input>
        </el-form-item>

        <el-form-item label="Пароль" prop="password1" :error="modelErrors.password1">
          <el-input type="password" v-model="signUpForm.password1" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="Подтверждение пароля" prop="password2" :error="modelErrors.password2">
          <el-input type="password" v-model="signUpForm.password2" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item label="Группа" prop="group" :error="modelErrors.group">
          <el-select v-model="signUpForm.group" placeholder="Группа" style="width: 100%">
            <el-option
                v-for="item in groups"
                :key="item.id"
                :label="item.title"
                :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item>
          <el-button @click="submitForm('signUpForm')" type="primary">Зарегистрироваться</el-button>
          <el-button @click="resetForm('signUpForm')">Сбросить</el-button>
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
      groups: [{id: 1, title: 'ОИБ-418'}, {id: 2, title: 'ОИБ-319'}, {id: 3, title: 'ОИБ-220'}],
      errorsList: [],

      signUpForm: {
        username: '',
        password1: '',
        password2: '',
        group: ''
      },
      rules: {
        username: [
          {required: true, message: 'Пожалуйста, введите имя пользователя', trigger: 'blur'},
        ],
        password1: [
          {required: true, min: 0, message: 'Минимальная длина пароля 8 символов', trigger: 'blur'},
          {validator: this.validatePassword1, trigger: 'blur'},
        ],
        password2: [
          {required: true, min: 0, message: 'Минимальная длина пароля 8 символов', trigger: 'blur'},
          {validator: this.validatePassword2, trigger: 'blur'},
        ],
        group: [
          {required: true, message: 'Пожалуйста, выберите группу', trigger: 'blur'}
        ],
      },
      modelErrors: {
        username: '',
        password1: '',
        password2: '',
        group: ''
      }
    }
  },
  methods: {
    validatePassword1(rule, value, callback) {
      if (value === '') {
        callback(new Error('Пожалуйста, введите пароль'));
      } else {
        if (this.signUpForm.password2 !== '') {
          this.$refs.signUpForm.validateField('password2');
        }
        callback();
      }
    },
    validatePassword2(rule, value, callback) {
      if (value === '') {
        callback(new Error('Пожалуйста, повторите пароль'));
      } else if (value !== this.signUpForm.password1) {
        callback(new Error('Пароли не совпадают!'));
      } else {
        callback();
      }
    },
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          const {errors, data} = await this.$sendForm('users/sign-up/', this.signUpForm, 'post', this.modelErrors)
          if (!errors) {
            this.$message.success('Вы успешно зарегистрировались')
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
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }

  }
}
</script>

<style scoped lang="scss">
.sign-up-form {
  max-width: 700px;
  margin: 0 auto;
}

.sign-up-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>