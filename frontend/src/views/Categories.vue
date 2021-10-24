<template>
  <el-container>
    <div class="categories">
      <el-row :gutter="30">
        <category-component
            v-for="(category, index) in categories"
            :key="index"
            :title="category.title"
            :description="category.description"
        />
      </el-row>
    </div>
  </el-container>

</template>

<script>
import CategoryComponent from "../components/CategoryComponent";

export default {
  name: "Categories",
  components: {
    CategoryComponent
  },
  data() {
    return {
      categories: [
          {title: 'admin', description: ''},
          {title: 'crypto', description: ''},
          {title: 'forensics', description: 'Компьютерно-криминалистическая экспертиза'},
          {title: 'web', description: 'Поиск и использование веб-уязвимостей'},
          {title: 'reverse', description: '(Reverse engineering) Анализ бинарного кода'},
      ]
    }
  }
}
</script>

<style scoped lang="scss">
  @import "../assets/css/functions.scss";

  .categories {
    max-width: toRem(1130);
    margin: 0 auto;
  }
</style>