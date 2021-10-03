<template>
  <div class="home">
    <index-page msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import IndexPage from '@/components/IndexPage'

export default {
  name: 'Home',
  components: {
    IndexPage
  }
}
</script>
