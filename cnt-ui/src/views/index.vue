<template>
  <div class="app-container home">
    <el-row :gutter="20">
      <el-col :sm="24" :lg="12" style="padding-left: 20px">
        <h2>欢迎来到CNT通用开发框架</h2>
        <p>当前版本: v{{ version }}</p>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
const version = ref("1.0.0");
</script>

<style scoped>
.home {
  padding: 20px;
}
h2 {
  color: #409eff;
  margin-bottom: 20px;
}
p {
  font-size: 16px;
  color: #666;
}
</style>
