<template>

  <el-skeleton :loading="isLoading" animated :count="20" style="width: 100%">
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
        <el-menu-item
            v-for="(object, index) in objectsList"
            @click="$emit('object-click', object)"
            :key="object.id || index"
            :index="index.toString()"
            class="objects-menu__item"
        >
          <span>{{ getTitle(object) }}  </span>
        </el-menu-item>
      </el-menu>
    </template>
  </el-skeleton>
</template>

<script>

export default {
  name: "ObjectsList",
  props: {
    isLoading: Boolean,
    objectsList: Array,
    titleName: String,
    getTitle: Function
  },
  emits: {
    'object-click': null
  }

}
</script>

<style scoped lang="scss">

.objects-menu {
  border: none;

  &__item {
    cursor: pointer;
  }
}

</style>