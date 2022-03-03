<template>
  <ul class="tasks__list">
    <task-component
      v-for="task in tasks"
      :key="`task-${task.id}`"
      :task="task"
      :current-category="currentCategory"
    />
  </ul>
</template>

<script>
import TaskComponent from "@/components/TaskComponent";

export default {
  name: "TasksList",
  props: {
    tasks: Array,
    currentCategory: Object,
  },
  components: {
    TaskComponent,
  },
};
</script>

<style scoped lang="scss">
.tasks {
  &__list {
    display: flex;
    flex-direction: column;

    @include _desktop {
      flex-direction: row;
      flex-wrap: wrap;
      margin-right: toRem(-21);
    }
  }
}
</style>