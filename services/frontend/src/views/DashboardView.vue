<template>
  <h1 class="m-4">Dashboard</h1>
  <div class="container mx-5 my-3">
    <div class="row">
      <div class="col-6">
        <h3>Balance</h3>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Period</th>
              <th scope="col">Expected Balance</th>
              <th scope="col">Balance Difference</th>
              <th scope="col">Real Balance</th>
            </tr>
          </thead>
          <tbody v-if="loaded" v-for="(total, index) in monthlyTotal">
            <tr>
              <td>{{ formatDate(total.date) }}</td>
              <td>{{ formatMoney(total.amount) }}</td>
              <td>
                {{ formatMoney(monthlyPayments[index].amount - total.amount) }}
              </td>
              <td>{{ formatMoney(monthlyPayments[index].amount) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-6">
        <h3>Daily Orders</h3>
        <DailyOrdersChart v-if="loaded" :dailyOrders="dailyOrders" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DailyOrdersChart from "@/components/DailyOrdersChart";

export default {
  name: "Dashboard",
  components: {
    DailyOrdersChart,
  },
  data() {
    return {
      monthlyPayments: [],
      monthlyTotal: [],
      dailyOrders: [],
      loaded: false,
    };
  },
  methods: {
    formatMoney(amount) {
      const formatter = new Intl.NumberFormat("es-CL", {
        style: "currency",
        currency: "clp",
      });
      return formatter.format(amount);
    },
    formatDate(date) {
      const dateObj = new Date(date);
      return dateObj.toLocaleDateString("default", {
        month: "long",
        year: "numeric",
      });
    },
    setData(monthlyPayments, monthlyTotal, dailyOrders) {
      this.monthlyPayments = monthlyPayments;
      this.monthlyTotal = monthlyTotal;
      this.dailyOrders = dailyOrders;
      this.loaded = true;
    },
    async fetchData() {
      axios
        .all([
          axios.get("/payments/monthly"),
          axios.get("/total/monthly"),
          axios.get("/orders/daily"),
        ])
        .then(
          axios.spread((monthlyPayments, monthlyTotal, dailyOrders) => {
            this.setData(
              monthlyPayments.data,
              monthlyTotal.data,
              dailyOrders.data
            );
          })
        );
    },
  },
  async created() {
    await this.fetchData();
  },
};
</script>
