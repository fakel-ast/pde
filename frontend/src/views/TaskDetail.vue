<template>
  <section class="section-task-detail">
    <div class="container task-detail-container">
      <div class="task-detail__content task-content">
        <h1 class="page-title only-desktop">
          {{ task.title }}
        </h1>
        <div class="task-content__description task-description">
          <p class="task-description__title">
            Описание задачи:
          </p>
          <div class="task-description__text" v-html="task.description">

          </div>
        </div>
        <div v-if="task.files" class="task-content__files task-files task-content-block">
          <div class="task-files__header">
            <p class="task-files__title task-content__title">Файл</p>
            <p class="task-files__title task-content__title">Размер файла</p>
          </div>
          <div class="task-files__footer">
            <ul class="task-files__list">
              <li
                v-for="file in task.files"
                :key="file.file"
                class="task-files__item"
              >
                <a :href="$host + file.file_link" class="task-files__file link">
                  {{ file.file }}
                </a>
                <p class="task-files__size">
                  {{ getFileSize(file.size) }}
                </p>
              </li>
            </ul>
          </div>
        </div>
        <div v-if="task.hints" class="task-content__hints task-hints task-content-block">
          <div class="task-hints__header" @click="isOpenHints = !isOpenHints">
            <p class="task-hints__title task-content__title">
              Подсказки
            </p>
            <div class="task-hints__info">
              <div class="task-hints__bubble task-hints__count">
                {{ task.hints.length }}
              </div>
              <div
                :class="{opened: isOpenHints}"
                class="task-hints__arrow"
              >
              </div>
            </div>
          </div>
          <slide-up-down tag="div" v-model="isOpenHints" :duration="durationTime" class="task-hints__content">
            <ul class="task-hints__list">
              <li
                v-for="(hint, index) in task.hints"
                :key="`task-hint-${hint.text}`"
                class="task-hints__item"
              >
                Подсказка {{ index + 1 }}: {{ hint.text }}
              </li>
            </ul>
          </slide-up-down>
        </div>
        <div class="task-content__answers task-answers task-content-block">
          <div class="task-answers__header">
            <p class="task-answers__title task-content__title">
              Ответ
            </p>
          </div>
          <div class="task-answers__not-auth not-auth">
            <span class="not-auth__text">Для этого&nbsp;</span>
            <a class="not-auth__link link" href="#">войдите или зарегистрируйтесь!</a>
          </div>
          <div class="task-answers__answer answer-form">
            <label for="answer" class="answer-form__title">
              Вставьте ответ в поле:
            </label>
            <form class="answer-form__form">
              <input id="answer" type="text" class="answer-form__input" name="answer" placeholder="Ваш ответ"/>
              <button class="button answer-form__button">Проверить</button>
            </form>
          </div>
          <div class="task-answers__old-answers old-answers">
            <p class="old-answers__title task-content__title">
              Мои ответы
            </p>
            <p class="old-answers__empty">
              Ваших ответов не найдено.
            </p>
            <ul class="old-answers__list">
              <li class="old-answers__item">
                <p class="old-answers__answer">Какой-то ответ</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status success-text">Верно</p>
              </li>
              <li class="old-answers__item">
                <p class="old-answers__answer">Какой-то ответ</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status error-text">Верно</p>
              </li>
              <li class="old-answers__item">
                <p class="old-answers__answer">Какой-то очень-очень длиннasdasdasdasdasdas</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status error-text">Верно</p>
              </li>
            </ul>
          </div>
        </div>
        <div class="task-content__answers task-answers task-content-block">
          <div class="task-answers__header">
            <p class="task-answers__title task-content__title">
              Ответ
            </p>
          </div>
          {{ code }}
          <div class="task-answers__answer answer-form code-form">
            <label for="code" class="answer-form__title">
              Вставьте ваш код ниже:
            </label>
            <form class="answer-form__form code-form__form">
              <textarea ref="codeTextArea" id="code" type="text" name="answer" placeholder="Ваш ответ"/>
              <button class="button code-form__button">Проверить</button>
            </form>
          </div>
          <div class="task-answers__old-answers old-answers">
            <p class="old-answers__title task-content__title">
              Мои ответы
            </p>
            <p class="old-answers__empty">
              Ваших ответов не найдено.
            </p>
            <ul class="old-answers__list">
              <li class="old-answers__item">
                <p class="old-answers__answer">Ответ #3 (2 строки)</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status success-text">Верно</p>
              </li>
              <li class="old-answers__item">
                <p class="old-answers__answer">Ответ #2 (2 строки)</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status error-text">Верно</p>
              </li>
              <li class="old-answers__item">
                <p class="old-answers__answer">Ответ #3 (2 строки)</p>
                <p class="old-answers__date">29.12.2021 20:25 GMT</p>
                <p class="old-answers__status error-text">Верно</p>
              </li>
            </ul>
          </div>
        </div>
        <div class="task-content__statistics task-statistics task-content-block">
          <div class="task-hints__header" @click="isOpenStatistics = !isOpenStatistics">
            <p class="task-hints__title task-content__title">
              Статистика
            </p>
            <div class="task-hints__info">
              <div
                :class="{opened: isOpenStatistics}"
                class="task-hints__arrow"
              >
              </div>
            </div>
          </div>
          <slide-up-down tag="div" v-model="isOpenStatistics" :duration="durationTime" class="task-statistics__content">
            <div class="task-statistics__static">
              <div class="task-statistics__success">
                <p class="task-statistics__title">
                  Правильные ответы - 541
                </p>
                <div class="task-statistics__progress task-statistics__progress-success"></div>
              </div>
              <div class="task-statistics__error">
                <p class="task-statistics__title">
                  Неправильные ответы - 3151
                </p>
                <div class="task-statistics__progress task-statistics__progress-error"></div>
              </div>
            </div>
          </slide-up-down>
        </div>
      </div>
      <h1 class="page-title only-mobile">Журналы</h1>
      <div class="task-detail__additional">
        <div class="task-detail__info">
          <p class="task-detail__status">
            Статус: {{ task.is_solved ? "решена" : "не решена" }}
          </p>
          <p class="task-detail__resolve-count">
            {{ `${getSolvedSuffix(task.solved_count)} ${task.solved_count} ${getUsersSuffix(task.solved_count)}` }}
          </p>
          <p class="task-detail__point-count">
            Очки: +{{ task.point_count }}
          </p>
        </div>
        <button class="task-detail__button button button-red">
          Сообщить об ошибке
        </button>
      </div>
    </div>
  </section>
</template>

<script>
const filesize = require("filesize");

import SlideUpDown from "vue3-slide-up-down";

// CodeMirror
import CodeMirror from "codemirror/lib/codemirror.js";
import "codemirror/addon/scroll/simplescrollbars";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/python/python";
import "@/assets/css/codemirror-theme.css";
import "codemirror/addon/scroll/simplescrollbars.css";

import "codemirror/addon/hint/show-hint.css";
import "codemirror/addon/hint/show-hint.js";
import "codemirror/addon/hint/anyword-hint";
import {Axios} from "@/assets/js/http-common";

export default {
  name: "TaskDetail",
  props: {
    getSolvedSuffix: Function,
    getUsersSuffix: Function,
  },
  components: {
    SlideUpDown,
  },
  data() {
    return {
      isOpenHints: false,
      isOpenStatistics: false,
      durationTime: 300,
      code: "",
      codeMirror: null,
      task: {},
    };
  },
  created() {
    this.getTaskDetail();
  },
  mounted() {
    if (this.$refs.codeTextArea) {
      this.codeMirror = CodeMirror.fromTextArea(this.$refs.codeTextArea, {
        mode: "python",
        lineNumbers: true,
        theme: "code-skill",
        indentUnit: 4,
        scrollbarStyle: "overlay",
      });
    }
  },
  methods: {
    async getTaskDetail() {
      try {
        const { data } = await Axios.get(
          `/categories/${this.$route.params.categorySlug}/tasks/${this.$route.params.taskId}/`,
        );
        this.task = data?.task || {};
      } catch (error) {
        console.error(error);
      }
    },
    getFileSize(size) {
      return filesize(size);
    },
  },
};
</script>

<style scoped lang="scss">

.section-task-detail {
  justify-content: space-between;
  padding-top: toRemMob(21);
  @include _desktop {
    padding-top: toRem(59);
  }
}

.task-detail {
  &-container {
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    @include _desktop {
      flex-direction: row;
    }
  }

  &__content {
    order: 2;
    width: 100%;
    margin-top: toRemMob(46);
    @include _desktop {
      max-width: toRem(873);
      order: 1;
      margin-top: 0;
    }
  }

  &__additional {
    display: flex;
    flex-direction: column;
    align-items: center;
    order: 1;
    @include _desktop {
      order: 2;
    }
  }

  &__info {
    display: flex;
    flex-direction: column;
    width: 100%;
    padding: toRemMob(37);
    border-radius: toRemMob(18);
    background-color: $dark-grey-color;
    font-size: toRemMob(21.2317);
    line-height: toRemMob(24);

    @include _desktop {
      min-width: toRem(315);
      max-width: toRem(315);
      padding: toRem(40);
      border-radius: toRem(19);
      font-size: toRemMob(22);
      line-height: toRemMob(25);
    }

    p:not(:first-child) {
      margin-top: toRemMob(15);
      @include _desktop {
        margin-top: toRem(16);
      }
    }
  }

  &__status {
    &.resolved {
      color: $sea-color;
    }
  }

  &__button {
    width: 100%;
    margin-top: toRem(21);
    @include _desktop {
      margin-top: toRem(32);
    }
  }

}

.task-content {

  &-block {
    border-radius: toRemMob(10);
    background-color: $dark-grey-color;
    @include _desktop {
      padding: toRem(30) toRem(38);
      border-radius: toRem(19);
      &:not(:first-child) {
        margin-top: toRem(31);
      }
    }
  }


  &__hints {

  }

  &__title {
    font-weight: 600;
    font-size: toRem(25);
    line-height: toRem(29);
  }

}

.task-description {
  &__title {
    margin-bottom: toRemMob(40);
    font-weight: 600;
    font-size: toRemMob(25);
    line-height: toRemMob(29);
    @include _desktop {
      margin-bottom: toRem(40);
      font-size: toRem(25);
      line-height: toRem(29);
    }
  }

  &__text {
    font-size: toRemMob(22);
    line-height: toRemMob(25);

    @include _desktop {
      font-size: toRem(22);
      line-height: toRem(25);
    }

    p {
      margin-bottom: toRemMob(27);
      @include _desktop {
        margin-bottom: toRem(32);
      }
    }

    ul {

    }

    li {

      &::before {
        content: "• "; /* Добавляем в качестве маркера символ */
      }

      &:not(:first-child) {
        margin-top: toRemMob(28);
        @include _desktop {
          margin-top: toRem(28);
        }
      }
    }
  }
}

.task-files {
  &__header {
    display: flex;
    padding-bottom: 22px;
    border-bottom: 1px solid $grey-color;
  }

  &__title {

    &:first-child {
      max-width: toRem(400);
      width: 100%;
    }
  }

  &__footer {
    margin-top: toRem(33);
  }

  &__list {
    display: flex;
    flex-direction: column;
  }

  &__item {
    display: flex;
    align-items: center;
    line-height: toRem(25);

    &:not(:first-child) {
      margin-top: toRem(32);
    }
  }

  &__file {
    flex-basis: toRem(400);
    color: $sea-color;
  }
}

.task-hints {
  &__header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
  }

  &__info {
    display: flex;
    align-items: center;
  }

  &__arrow {
    width: toRem(22);
    height: toRem(12);
    margin-left: toRem(25);
    background: url("../assets/images/task_detail/arrow.svg") no-repeat center center;
    transition: transform .3s ease;

    &.opened {
      transform: rotate(180deg);
    }
  }

  &__bubble {
    max-height: toRem(26);
    padding: toRem(3) toRem(15);
    line-height: toRem(25);
    background-color: $blue-color;
    border-radius: toRem(25);
  }

  &__list {
    display: flex;
    flex-direction: column;
    align-items: start;
    padding-top: toRem(26);
  }

  &__item {
    &:not(:first-child) {
      margin-top: toRem(26);
    }
  }
}

.task-answers {
  &__header {
    margin-bottom: toRem(30);
  }

  &__old-answers {
    margin-top: toRem(46);
  }

  &__not-auth {
    margin-top: toRem(26);
    font-size: toRem(20);
    line-height: toRem(24);
  }
}

.not-auth {
  &__link {
    color: $sea-color;
  }
}

.answer-form {
  &__title {
    display: block;
  }

  &__form {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: toRem(17);
  }

  &__input {
    flex-basis: 100%;
    padding: toRem(11) toRem(24) toRem(8) toRem(24);
    border: 1px solid $grey-color;
    border-radius: toRem(25);
    background-color: transparent;
    color: $white-color;
    outline: none;
    font-size: toRem(22);
    line-height: toRem(25);

    &::placeholder {
      color: $grey-color;
    }
  }

  &__button {
    margin-left: toRem(20);
  }
}

.old-answers {
  &__title {
    margin-bottom: toRem(17);
  }

  &__empty {
    margin-top: toRem(17);
    color: $grey-color;
  }

  &__list {
    display: flex;
    flex-direction: column;
    margin-top: toRem(26);
  }

  &__item {
    display: flex;
    align-items: center;
    padding-bottom: toRem(18);
    border-bottom: 1px solid $grey-color;

    &:not(:first-child) {
      margin-top: toRem(18);
    }
  }

  &__answer {
    flex-basis: toRem(277);
    white-space: nowrap; /* Текст не переносится */
    overflow: hidden; /* Обрезаем всё за пределами блока */
    text-overflow: ellipsis; /* Добавляем многоточие */
    padding-right: toRem(20);
  }

  &__date {
    color: $grey-color;
  }

  &__status {
    margin-left: auto;
  }
}

.code-form {
  &__form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: toRem(20);
  }

  &__button {
    margin-top: toRem(32);
  }
}

.task-statistics {
  &__static {
    display: flex;
    flex-direction: column;
    padding-top: toRem(41);
  }

  &__title {
    margin-bottom: toRem(29);
  }

  &__error {
    margin-top: toRem(44);
  }

  &__progress {
    position: relative;
    width: 100%;
    height: toRem(19);
    background: $grey-color;
    border-radius: toRem(33);

    &::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      border-radius: toRem(33);
    }

    &-success {
      &::before {
        width: 30%;
        background-color: $green-color;
      }
    }

    &-error {
      &::before {
        width: 70%;
        background-color: $red-color;
      }
    }
  }

}

</style>

<style lang="scss">

.task-description {


  &__text {
    p {
      margin-bottom: toRemMob(27);
      @include _desktop {
        margin-bottom: toRem(32);
      }
    }

    ul {

    }

    li {

      &::before {
        content: "• "; /* Добавляем в качестве маркера символ */
      }

      &:not(:first-child) {
        margin-top: toRemMob(28);
        @include _desktop {
          margin-top: toRem(28);
        }
      }
    }
  }
}

.CodeMirror {
  width: 100%;
  height: toRem(453);
  border-radius: toRem(19);
}
</style>
