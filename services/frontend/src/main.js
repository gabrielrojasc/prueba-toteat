import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = process.env.VUE_APP_API_URL;

createApp(App).use(store).use(router).mount("#app");
