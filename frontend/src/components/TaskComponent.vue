<template>
  <li
    :class="{solved: task.is_solved}"
    class="task__item"
  >
    <router-link class="task__link" :to="{ name: 'TaskDetail', params: { ...$route.params, taskId: task.id } }">
      <div class="task__header">
        <p class="task__title">{{ task.title }}</p>
        <p class="task__points">+{{ task.point_count }} очков</p>
      </div>
      <div class="task__footer">
        <p class="task__solvings">
          {{
            task.is_solved
              ? `Решено`
              : `${getSolvedSuffix(task.solved_count)} ${task.solved_count} ${getUsersSuffix(task.solved_count)}`
          }}
        </p>
      </div>
    </router-link>
  </li>
</template>

<script>
export default {
  name: "TaskComponent",
  props: {
    task: Object,
    currentCategory: Object,
    getSolvedSuffix: Function,
    getUsersSuffix: Function,
  },
  methods: {},
};
</script>

<style scoped lang="scss">

.task {
  &__item {
    padding: toRemMob(17) toRemMob(24) toRemMob(14) toRemMob(21);

    background-color: $dark-grey-color;
    border-radius: 12.815px;
    transition: background-color 0.2s ease;

    &.solved {
      color: $white-color;

      .task__solvings {
        color: $green-color;
      }
    }

    &:hover {
      background-color: $grey-color-three;

      .task__points {
        color: $white-color;
      }
    }

    &:not(:first-child) {
      margin-top: toRemMob(18);
    }

    @include _desktop {
      width: toRem(427);
      padding: toRemMob(24) toRemMob(34) toRemMob(19) toRemMob(30);
      margin-right: toRem(20);
      border-radius: toRem(18);

      &:not(:first-child) {
        margin-top: 0;
      }

      &:not(:nth-child(-n + 3)) {
        margin-top: toRem(21);
      }
    }
  }

  &__link {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  &__header {
    display: flex;
    justify-content: space-between;
    margin-bottom: toRemMob(21);

    @include _desktop {
      margin-bottom: toRem(30);
    }
  }

  &__title {
    font-weight: 600;
    font-size: toRemMob(17.7986);
    line-height: toRemMob(20);
    color: $white-color;
    @include _desktop {
      font-size: toRem(25);
      line-height: toRem(29);
    }
  }

  &__points {
    font-size: toRemMob(15.6628);
    line-height: toRemMob(18);
    color: $grey-color-two;
    transition: .2s color ease;
    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }
  }

  &__solvings {
    font-size: toRemMob(15.6628);
    line-height: toRemMob(18);
    color: $white-color;

    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }
  }
}
</style>