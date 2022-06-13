<template>
  <div>
    <ul class="greenhouse-sliders__list">
      <li class="greenhouse-sliders__item greenhouse-sliders__header">
        <div class="greenhouse-sliders__column">
          Сортировка
        </div>
        <div class="greenhouse-sliders__column">
          Фото мобилки
        </div>
        <div class="greenhouse-sliders__column">
          Фото десктоп
        </div>
        <div class="greenhouse-sliders__column">
          Фото экстра десктоп
        </div>
        <div class="greenhouse-sliders__column">
          Удаление
        </div>
      </li>

      <draggable
        :list="slides"
        handle=".handle"
        item-key="currentConfiguration.attributes"
        class="draggable-list"
        v-bind="dragOptions"
      >
        <template class="" #item="{ element }">
          <li class="greenhouse-sliders__item">
            <div class="greenhouse-sliders__column additional-products__handle handle">
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
              <div class="handle__line"></div>
            </div>
            <div class="greenhouse-sliders__column">
              <el-upload
                action="/"
                drag
                :before-upload="(file) => uploadImage({file, slide: element, fieldName: 'image_mobile'})"
              >
                <div class="slider-image">
                  <img :src="getImage(element, 'image_mobile')" class="avatar-desktop">
                </div>
              </el-upload>
            </div>
            <div class="greenhouse-sliders__column">
              <el-upload
                action="/"
                drag
                :before-upload="(file) => uploadImage({file, slide: element, fieldName: 'image_desktop'})"
              >
                <div class="slider-image">
                  <img :src="getImage(element, 'image_desktop')" class="avatar-desktop">
                </div>
              </el-upload>
            </div>
            <div class="greenhouse-sliders__column">
              <el-upload
                action="/"
                drag
                :before-upload="(file) => uploadImage({file, slide: element, fieldName: 'image_extra_desktop'})"
              >
                <div class="slider-image">
                  <img :src="getImage(element, 'image_extra_desktop')" class="avatar-desktop">
                </div>
              </el-upload>
            </div>

            <div class="greenhouse-sliders__column column__delete">
              <el-popconfirm @confirm="removeSlide(element)" title="Вы уверены?">
                <template #reference>
                  <span class="material-symbols-rounded buttons__delete">
                    delete
                  </span>
                </template>
              </el-popconfirm>

            </div>
          </li>
        </template>
      </draggable>
    </ul>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import {ElMessage} from "element-plus";

export default {
  name: "GreenhouseSliderDragNDrop",
  props: {
    slides: Array,
    getImage: Function
  },
  components: {
    draggable
  },
  data() {
    return {
      dragOptions: {
        animation: 200,
      }
    };
  },
  methods: {
    removeSlide(slide) {
      this.$emit("remove", slide.id);
    },
    uploadImage(uploadData) {
      if(uploadData.file.size > 1500000){
        ElMessage({
          message: `Недопустимо загружать картинки больше 1.5 Мегабайт`,
          type: 'error'
        })
      }else{
        this.$emit("upload-image", uploadData);
      }
    }
  }
};
</script>

<style scoped lang="scss">
.greenhouse-sliders {
  &__list {
    display: flex;
    flex-direction: column;
    border: 1px solid #eee;
    border-radius: 5px;
  }

  &__header {
    font-weight: 600;
    position: sticky;
    top: 0;
    background-color: #FFFFFF;
    z-index: 100;
  }

  &__item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    text-align: left;

    .draggable-list > &:nth-of-type(odd) {
      background-color: #efefef;
    }
  }

  &__column {
    width: 100%;
    min-width: 100px;
    padding: 10px;

    &:first-child {
      margin-left: 30px;
    }

    &:last-child {
      width: unset;
    }
  }
}

.slider-image {
  min-width: 280px;
  height: auto;
  min-height: 166px;

  img {
    display: block;
  }
}

</style>