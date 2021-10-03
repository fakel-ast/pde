<template>
  <el-input v-model="input" placeholder="Please input" />
  {{ input }}
</template>

<script>
import { ref } from 'vue'

export default {
  name: "Tasks",
  setup() {
    return {
      input: ref(''),
    }
  },
}
</script>

<style scoped>

</style>