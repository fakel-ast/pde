<template>
  <el-row>
    <el-col :span="11">
      <h3 class="additional-products__category-title">Выбранные</h3>
      <draggable
        class="additional-products__list"
        tag="ul"
        :list="selectedList"
        handle=".handle"
        group="draggable-group"
        v-bind="dragOptions"
        itemKey="category"
      >
        <template #item="{ element }">
          <li class="additional-products__item">
            <div class="additional-products__handle handle">
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
            </div>
            <div class="additional-products__title">
              {{ replaceHTML(getTitle(element)) }}
            </div>
          </li>
        </template>
      </draggable>
    </el-col>
    <el-col :span="11" :offset="2">
      <h3 class="additional-products__category-title">Доступные</h3>
      <draggable
        class="additional-products__list"
        tag="ul"
        :list="unselectedList"
        group="draggable-group"
        handle=".handle"
        v-bind="dragOptions"
        itemKey="category"
      >
        <template #item="{ element }">
          <li class="additional-products__item">
            <div class="additional-products__handle handle">
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
            </div>
            <div class="additional-products__title">
              {{ replaceHTML(getTitle(element)) }}
            </div>
          </li>
        </template>
      </draggable>
    </el-col>
  </el-row>


</template>
<script>
import draggable from "vuedraggable";

export default {
  name: "TwoListDragNDrop",
  props: {
    selectedList: Array,
    unselectedList: Array,
    getTitle: Function
  },
  inject: ['replaceHTML'],
  emits: {},
  components: {
    draggable
  },
  data() {
    return {
      dragOptions: {
        animation: 200,
      }
    }
  },
};
</script>

<style scoped lang="scss">
.additional-products {
  &__list {
    display: flex;
    flex-direction: column;
    min-height: 100px;
    height: 100%;
  }

  &__item {
    display: flex;
    align-items: center;
    padding: 12px 20px;
    border: 1px solid rgba(0, 0, 0, 0.125);

    &:first-child {
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
    }

    &:last-child {
      border-bottom-left-radius: 5px;
      border-bottom-right-radius: 5px;
    }
  }

  &__title {
    margin-left: 40px;
  }

  &__category-title {
    font-weight: 600;
    margin: 10px 5px;
  }
}
</style>