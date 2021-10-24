<template>
  <el-col
      :span="cardSpan"
      class="category__container"
  >

    <el-popover
        placement="bottom"
        :width="200"
        trigger="hover"
        :content="description"
        :disabled="description.length === 0"
        :show-after="90"
    >
      <template #reference>
        <el-card class="category__item" shadow="hover">
          <template #header>
            <div class="category__title">
              {{ title }}
            </div>
          </template>
          <div class="category__bottom">
            <p class="category__tasks">
              60 задач
            </p>
            <div class="category__next">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34" class="category__icon">
                <g transform="translate(-617.419 -1116.68)">
                  <g transform="translate(618.419 1117.68)">
                    <g>
                      <path d="M16,0A16,16,0,1,1,0,16,16,16,0,0,1,16,0Z" fill="none" stroke="#f63"
                            stroke-width="2"></path>
                    </g>
                    <path d="M621.475,1126.156l6.121,7.564-6.121,7.435" transform="translate(-607.762 -1117.317)"
                          fill="none" stroke="#f63" stroke-miterlimit="10" stroke-width="2"></path>
                  </g>
                </g>
              </svg>
            </div>
          </div>
        </el-card>
      </template>
    </el-popover>


  </el-col>
</template>

<script>

export default {
  name: "CategoryComponent",
  props: {
    cardSpan: {
      type: Number,
      default: 6
    },
    description: String,
    title: String
  },

}
</script>

<style lang="scss">
@import "../assets/css/functions.scss";


.el-card {
  background: #4c5054 url("../assets/img/test_img_1.jpg") center;

  &__header {
    border: none;
  }
}

.category {
  &__container {
    &:not(:nth-child(-n+4)) {
      margin-top: toRem(30);
      width: toRemMob(200);
    }
  }

  &__item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: toRem(260);
    width: toRem(260);
    color: #fff;
    cursor: pointer;


    &:hover {
      transform: scale(1.05);
    }
  }

  &__title {
    font-size: toRem(20);
    font-weight: bold;
  }

  &__bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__icon {
    width: 24px;
    height: auto;
  }

}

.el-popover.el-popper {
  word-break: break-word;
}

</style>