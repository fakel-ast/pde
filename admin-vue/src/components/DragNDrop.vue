<template>
  <div>
    <ul class="table-categorys">
      <li class="table-categorys-title">
        <div
          v-for="(item) in header"
          :key="item"
          class="column"
        >
          {{ item }}
        </div>
      </li>

      <draggable
        :list="draggableArray"
        handle=".handle"
        item-key="currentConfiguration.attributes"
        class="draggable-list"
        v-bind="dragOptions"
      >
        <template class="" #item="{ element }">
          <li>
            <div class="column column__draggable">
              <div class="draggable-list__handle-icon handle pointer">
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
              </div>
            </div>
            <div class="column" v-for="(item,i) in fields" :key="i">
              {{ element[item] ? element[item][language] : "" }}
            </div>
            <div class="column column__delete">
              <span @click="removeElement(element)"
                    class="material-symbols-rounded buttons__delete">delete
              </span>
            </div>
          </li>
        </template>
      </draggable>
    </ul>
  </div>
</template>

<script>
import draggable from 'vuedraggable';

export default {
  emits: {
    "remove": null,
  },
  props: {
    draggableArray: Array,
    language: String,
    fields: Array,
    header: Array,
  },
  components: {
    draggable,
  },
  data() {
    return {
      dragOptions: {
        animation: 200,
      }
    }
  },
  methods: {
    removeElement(element) {
      this.$emit('remove', element)
    }
  }
}
</script>

<style lang="scss" scoped>
.pointer {
  cursor: move;
}

.table-categorys {
  text-align: left;
  border: 1px solid #eee;
  table-layout: fixed;
  width: 100%;
  margin-bottom: 20px;

  &-title {
    font-weight: bold;
  }

  > li:nth-of-type(odd) {
    background-color: #efefef;
  }

  li {
    display: flex;
    align-items: center;
    justify-content: space-between;

    .column {
      width: 100%;
      min-width: 100px;
      padding: 10px;

      &:last-child, &:first-child {
        width: unset;
      }

      &:first-child {
        margin-left: 30px;
        width: unset;
      }



      &-drag {
        width: 50px;
        padding: 20px;
        cursor: pointer;
      }

    }
  }
}

.draggable-list {
  li:nth-child(even) {
    background-color: #efefef;
  }

  &__handle-icon {
    display: flex;
    flex-direction: column;
    align-items: start;

    .triangle-top {
      border-radius: 2px;
      width: 0;
      height: 0;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-bottom: 6px solid #8a8a8a;
    }

    .triangle-bottom {
      width: 0;
      height: 0;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 6px solid #8a8a8a;
    }

    .line {
      border-radius: 2px;
      width: 19px;
      height: 3px;
      background-color: #8a8a8a;
      margin: 1px 0;
    }
  }
}

</style>
