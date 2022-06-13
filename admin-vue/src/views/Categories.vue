<template>
  <el-scrollbar height="calc(100vh - 100px)" class="scrollbar">
    <el-table :data="categories" style="width: 100%">
      <el-table-column prop="date" label="Название">
        <template #default="scope">
          <el-input v-model="scope.row.title" placeholder="Название">
          </el-input>
        </template>
      </el-table-column>
      <el-table-column prop="date" label="Slug (ЧПУ)">
        <template #default="scope">
          <el-input v-model="scope.row.slug" placeholder="Slug">
          </el-input>
        </template>
      </el-table-column>
      <el-table-column prop="date" label="Активность">
        <template #default="scope">
          <el-checkbox label="Показывать" v-model="scope.row.active"></el-checkbox>
        </template>
      </el-table-column>
    </el-table>
    <el-affix position="bottom" :offset="20">
      <el-row :gutter="24">
        <el-col :span="3">
          <el-button @click="saveCategories" class="button button_save button_full-width " type="success">
            Сохранить
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button @click="addCategories" class="button button_add button_full-width " type="primary">
            Добавить
          </el-button>
        </el-col>
      </el-row>
    </el-affix>
  </el-scrollbar>
</template>

<script>
import {Axios} from "@/http-common";
import {ElMessage} from "element-plus";

export default {
  name: "Categories",
  data() {
    return {
      categories: null,
    };
  },
  created() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      this.categories = await Axios.get("categories/").then(({ data }) => data.categories || []);
    },
    async saveCategories() {
      try {
        await Axios.post("categories/", { categories: this.categories });
        ElMessage({
          message: `Успешно сохранено`,
          type: "success",
        });
      } catch (error) {
        console.error(error);
        ElMessage({
          message: `Ошибка сохранения ${error}`,
          type: "error",
        });
      }


    },
    addCategories() {
      this.categories.push({
        id: 0,
        title: null,
        slug: null,
        active: false
      })
    }
  },
};
</script>

<style scoped>

</style>