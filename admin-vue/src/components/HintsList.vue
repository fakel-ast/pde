<template>
  <el-scrollbar height="calc(100vh - 100px)" class="scrollbar">
    <el-skeleton :loading="!categoryHints.length" animated :count="20" style="width: 100%">
      <template #template>
        <div style="padding: 14px;">
          <el-skeleton-item variant="text"/>
        </div>
      </template>
      <template #default>
        <el-menu
          default-active=""
          class="objects-menu"
        >
          <h3 class="hint__category">Название атрибутов</h3>

          <el-menu-item
            v-for="(categoryHint, index) in categoryHints"
            :key="categoryHint.id"
            :index="`category-hint-${index}`"
            class="objects-menu__item"
            @click="$emit('change-current-hint', categoryHint)"
          >
            <span>{{ getCategoryHintTitle(categoryHint) }}  </span>
          </el-menu-item>
          <h3 v-if="valueHints" class="hint__category">Значение атрибутов</h3>
          <el-menu-item
            v-for="(valueHint, index) in valueHints"
            :key="valueHint.id"
            :index="`value-hint-${index}`"
            class="objects-menu__item"
            @click="$emit('change-current-hint', valueHint)"
          >
            <span>{{ getValueHintTitle(valueHint) }}  </span>
          </el-menu-item>
        </el-menu>
      </template>
    </el-skeleton>

  </el-scrollbar>
</template>

<script>

export default {
  name: "HintsList",
  components: {},
  emits: {
    "change-current-hint": null
  },
  props: {
    categoryHints: Array,
    defaultLanguage: String,
    valueHints: Array,
  },
  methods: {
    getCategoryHintTitle(hint) {
      if (!hint.attribute_category) return "";
      const greenhouseShortTitle = hint.greenhouse_title.replace("«Green Diamond» ", "");
      return `${hint.attribute_category[this.defaultLanguage]} - ${greenhouseShortTitle}`;
    },
    getValueHintTitle(hint) {
      if (!hint.attribute_value) return "";
      const greenhouseShortTitle = hint.greenhouse_title.replace("«Green Diamond» ", "");
      return `${hint.attribute_value[this.defaultLanguage]} - ${greenhouseShortTitle}`;
    }
  }
};
</script>

<style scoped lang="scss">
.hint {
  &__category {
    padding: 12px 20px;
    font-size: 20px;
    font-weight: 600;
  }
}
</style>