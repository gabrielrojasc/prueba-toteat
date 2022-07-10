<template>
  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

export default {
  name: "DailyOrdersChart",
  components: { Line },
  props: {
    chartId: {
      type: String,
      default: "bar-chart",
    },
    datasetIdKey: {
      type: String,
      default: "label",
    },
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 250,
    },
    cssClasses: {
      default: "",
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    dailyOrders: Array,
  },
  data() {
    return {
      chartData: {},
      chartOptions: {
        mantainAspectRatio: false,
        responsive: true,
        backgroundColor: "#f87979",
        pointStyle: "rectRot",
        pointRadius: 6,
        pointHoverRadius: 10,
      },
    };
  },
  created() {
    const dates = this.dailyOrders.map((order) => order.date);
    const counts = this.dailyOrders.map((order) => order.count);
    this.chartData = {
      labels: dates,
      datasets: [
        {
          label: "Orders",
          data: counts,
        },
      ],
    };
  },
};
</script>
