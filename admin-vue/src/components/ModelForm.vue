<template>
  <el-skeleton
      :loading="isLoading"
      animated
  >
    <template #template>
      <el-row
          :gutter="20"
          :align="'middle'"
      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>

      </el-row>
      <el-row
          :gutter="20"
          :align="'middle'"

      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>

      </el-row>
      <el-row
          :gutter="20"
          :align="'middle'"

      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>

      </el-row>

      <el-row
          :gutter="20"
          :align="'middle'"

      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="image" style="width: 360px; height: 180px; margin-bottom: 22px;"/>
        </el-col>
      </el-row>
      <el-row
          :gutter="20"
          :align="'middle'"

      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="image" style="width: 360px; height: 180px; margin-bottom: 22px;"/>
        </el-col>
      </el-row>
      <el-row
          :gutter="20"
          :align="'middle'"

      >
        <el-col
            :span="8"
        >
          <el-skeleton-item variant="text" style="height: 40px; margin-bottom: 22px;"/>
        </el-col>
        <el-col :span="16">
          <el-skeleton-item variant="image" style="width: 360px; height: 180px; margin-bottom: 22px;"/>
        </el-col>
      </el-row>


    </template>
    <template #default>
      <slot name="content">
      </slot>
    </template>
  </el-skeleton>
</template>

<script>
export default {
  name: "ModelForm",
  props: {
    'isLoading': Boolean,

  }
}
</script>

<style scoped>

</style>