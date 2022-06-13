<template>
  <div class="translate-fields">
    <h4 class="translate-fields__title" v-once v-if="!isNotUseTitle">
      <template v-if="fieldTitle && fieldTitle.length">
        {{ fieldTitle }}
      </template>
      <template v-else>
        {{ replaceHTML(modelValue.ru) }}
      </template>
    </h4>
    <input
      v-for="translateField in Object.keys(modelValue)"
      @input="changeValue(translateField, $event.target.value)"
      :key="`${translateField}`"
      :value="modelValue[translateField]"
      :placeholder="modelValue[translateField] ? modelValue[translateField] : `Перевод для ${translateField}`"
      class="translate-fields__input"
    />
  </div>
</template>

<script>
export default {
  name: "TranslateField",
  props: {
    modelValue: Object,
    isNotUseTitle: Boolean,
    fieldTitle: String,
    fieldName: {
      type: String,
      default: 'title'
    }
  },
  inject: ['replaceHTML'],
  methods: {
    changeValue(valueName, newValue) {
      const modelValueCopy = Object.assign({}, this.modelValue);
      modelValueCopy[valueName] = newValue;
      this.$emit('update:modelValue', modelValueCopy)
    },
  }
}
</script>

<style scoped lang="scss">
.translate-fields {
  display: flex;
  flex-direction: column;
  width: 100%;

  &__input {
    padding: 0 15px;
    line-height: 40px;
    height: 40px;
    color: #606266;
    border-radius: 4px;
    border: 1px solid #c0c4cc;
    margin-bottom: 10px;
    transition: border-color .2s ease-in-out;

    &:focus {
      border-color: #409eff;
    }

    &::placeholder {
      opacity: 0.5;
    }

  }

  &__title {
    margin: 7px 0;
    font-weight: 600;
    font-size: 18px;
  }
}
</style>