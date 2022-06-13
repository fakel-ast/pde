<template>
  <h1>Code skills admin panel</h1>
</template>
<script>

export default {
  name: "GreenhousePage",
  data() {
    return {
      baseJson: {},
    };
  },
};
</script>
<style lang="scss">
.el-image-viewer__img{
  width: 70%;
}
.list-inline{
  position: relative;
  bottom: 100px;
  right: 40px;
  display: flex;
  justify-content: end;
}
.el-carousel__button{
  width: 10px;
  height: 10px;
  background-color: aqua;
  border-radius: 50%;
}
.el-carousel__arrow{
  background-color: #494949;
  box-shadow: 0 0 0 2px #ffffff;
}
.el-divider__text {
  font-size: 18px;
  line-height: 18px;
  font-weight: 500;
}
.el-scrollbar__body {
  overflow-x: hidden;
}

</style>
<style scoped lang="scss">
h1 {
  font-size: 35px;
  font-weight: 600;
  line-height: 1;

  + p {
    margin-top: 40px;
  }

  .el-icon {
    font-size: inherit;
    font-weight: inherit;
    line-height: inherit;
  }
}

h2 {
  font-size: 25px;
  font-weight: 500;
  line-height: 1;
  text-align: center;

  + h3 {
    margin-top: 30px;
  }

  .el-icon {
    font-size: inherit;
    font-weight: inherit;
    line-height: inherit;
    top: 2px;
  }

  + .el-row {
    margin-top: 30px;
  }
}

h3 {
  font-size: 20px;
  font-weight: 500;
  line-height: 1;

  .el-icon {
    font-size: inherit;
    font-weight: inherit;
    line-height: inherit;
  }

  + .el-row {
    margin-top: 15px;
  }

  + .el-divider {
    margin-top: 30px;
  }

}

p {
  font-size: 18px;
  line-height: 27px;
  font-weight: 300;

  + p {
    margin-top: 15px;
  }

  + h2 {
    margin-top: 40px;
  }

  b {
    font-weight: 700;
  }
}

.el-row {
  + .el-row {
    margin-top: 60px;
  }
}

.el-divider {
  + h2 {
    margin-top: 100px;
  }

  + h3 {
    margin-top: 30px;
  }
}

.el-button {
  .el-icon {
    font-size: inherit;
    line-height: inherit;
    top: 2px;
  }
}

//cat start
#bongo-cat {
  width: 100%;
  max-width: 600px;
  margin: 60px auto 0 auto;
  display: block;
}

.typing-animation {
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-duration: 1200ms;
}

path#f1-l1 {
  animation-name: typing-f1-l1;
}

path#f1-l2 {
  animation-name: typing-f1-l2;
}

path#f1-l3 {
  animation-name: typing-f1-l3;
}

path#f2-l4 {
  animation-name: typing-f2-l4;
}

path#f2-l5 {
  animation-name: typing-f2-l5;
}

path#f2-l6 {
  animation-name: typing-f2-l6;
}

path#f3-l7 {
  animation-name: typing-f3-l7;
}

path#f3-l8 {
  animation-name: typing-f3-l8;
}

path#f3-l9 {
  animation-name: typing-f3-l9;
}

@keyframes typing-f3-l9 {
  0% {
    d: path("M8,25L8,25");
  }
  82% {
    d: path("M8,25L8,25");
  }
  92% {
    d: path("M8,25L96,25");
  }
  100% {
    d: path("M8,25L96,25");
  }
}

@keyframes typing-f3-l8 {
  0% {
    d: path("M8,13L8,13");
  }
  68% {
    d: path("M8,13L8,13");
  }
  82% {
    d: path("M8,13L146,13");
  }
  100% {
    d: path("M8,13L146,13");
  }
}

@keyframes typing-f3-l7 {
  0% {
    d: path("M0,1L0,1");
  }
  60% {
    d: path("M0,1L0,1");
  }
  68% {
    d: path("M0,1L96,1");
  }
  100% {
    d: path("M0,1L96,1");
  }
}

@keyframes typing-f2-l6 {
  0% {
    d: path("M8,25L8,25");
  }
  54% {
    d: path("M8,25L8,25");
  }
  60% {
    d: path("M8,25L69,25");
  }
  100% {
    d: path("M8,25L69,25");
  }
}

@keyframes typing-f2-l5 {
  0% {
    d: path("M8,13L8,13");
  }
  44% {
    d: path("M8,13L8,13");
  }
  54% {
    d: path("M8,13L114,13");
  }
  100% {
    d: path("M8,13L114,13");
  }
}

@keyframes typing-f2-l4 {
  0% {
    d: path("M0,1L0,1");
  }
  30% {
    d: path("M0,1L0,1");
  }
  44% {
    d: path("M0,1L136,1");
  }
  100% {
    d: path("M0,1L136,1");
  }
}

@keyframes typing-f1-l3 {
  0% {
    d: path("M8,25L8,25");
  }
  24% {
    d: path("M8,25L8,25");
  }
  30% {
    d: path("M8,25L61,25");
  }
  100% {
    d: path("M8,25L61,25");
  }
}

@keyframes typing-f1-l2 {
  0% {
    d: path("M8,13L8,13");
  }
  14% {
    d: path("M8,13L8,13");
  }
  24% {
    d: path("M8,13L124,13");
  }
  100% {
    d: path("M8,13L124,13");
  }
}

@keyframes typing-f1-l1 {
  0% {
    d: path("M0,1L0,1");
  }
  14% {
    d: path("M0,1L160,1");
  }
  100% {
    d: path("M0,1L160,1");
  }
}

#paw-right--up,
#paw-right--down,
#paw-left--up,
#paw-left--down {
  animation: blink 300ms infinite;
}

#paw-right--up,
#paw-left--down {
  animation-delay: 150ms;
}

@keyframes blink {
  0% {
    opacity: 0;
  }
  49% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
}

#laptop__code {
  transform: rotateX(-37deg) rotateY(-46deg) rotateZ(-23deg) translateX(8px) translateY(20px) translateZ(-50px);
  width: 100px;
}

.translate {
  &__title {
    font-size: var(--el-font-size-extra-large);
    font-weight: 600;
    margin-bottom: 10px;

    &:not(:first-child) {
      margin-top: 10px;
    }
  }
}

.translate-action {
  padding: 30px 0 0 30px;
}

//cat end
.line-draggable {
  display: inline;
  width: 100px;
  height: 100px;
  background-color: #f56c6c;
}

.draggable-list {
  li:nth-child(even) {
    background-color: #efefef;
  }

  &__handle-icon {
    display: flex;
    flex-direction: column;
    align-content: flex-start;
    width: 20px !important;
    margin: unset;

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