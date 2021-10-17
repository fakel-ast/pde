import {createApp} from 'vue'
import ElementPlus from 'element-plus'
import ru from 'element-plus/es/locale/lang/ru'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import {Axios} from "@/http-common";


const app = createApp(App)

app.config.globalProperties.$commonDuration = 5000
app.config.globalProperties.$sendForm = async function (url, data, method = 'post', modelErrors = {}) {
    try {

        const responce = await Axios({
            url: url,
            method: method,
            data: data
        })
        if (responce.status >= 200 && responce.status <= 300) {
            if (!responce.data.errors) {
                return {'errors': false, data: responce.data}
            } else {
                const errors = responce.data;
                modelErrors = {}
                if (errors.errors_dict && Object.entries(errors.errors_dict).length) {
                    Object.entries(errors.errors_dict).forEach(([field, error]) => {
                        modelErrors[field] = typeof error === 'object' ? error[0].message : error
                    })
                }
                if (errors.messages && errors.messages.length) {
                    errors.messages.forEach(message => {
                        setTimeout(
                            () => {
                                this.$message({
                                    type: 'error',
                                    message: message,
                                    duration: this.$commonDuration
                                })
                            }, 0
                        )
                    })
                }
                return {'errors': true, data: {modelErrors: modelErrors, errors: errors}}
            }
        } else {
            this.$message.error(`Что-то пошло не так при отправке запроса`)
        }
    } catch (error) {
        this.$message.error(`Что-то пошло не так при отправке запроса`)
    }
}
app.use(ElementPlus, {locale: ru}).use(router).mount('#app')
