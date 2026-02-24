import { createApp } from "vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import locale from "element-plus/es/locale/lang/zh-cn";

import "@/assets/styles/index.scss";

import App from "./App";
import router from "./router";

import "./permission";

import {
  parseTime,
  resetForm,
  handleTree,
  selectDictLabel,
  selectDictLabels,
} from "@/utils/conventional";

const app = createApp(App);

app.config.globalProperties.parseTime = parseTime;
app.config.globalProperties.resetForm = resetForm;
app.config.globalProperties.handleTree = handleTree;
app.config.globalProperties.selectDictLabel = selectDictLabel;
app.config.globalProperties.selectDictLabels = selectDictLabels;

app.use(router);
app.use(ElementPlus, {
  locale: locale,
  size: "default",
});

app.mount("#app");
