<template>
  <h1 class="m-4">Dashboard</h1>
  <div class="container-fluid px-5">
    <div class="row justify-content-center">
      <div class="col">
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
      <div class="col">
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

<style scoped>
@media only screen and (max-width: 760px),
  (min-device-width: 768px) and (max-device-width: 1024px) {
  /* Force table to not be like tables anymore */
  table,
  thead,
  tbody,
  th,
  td,
  tr {
    display: block;
  }

  /* Hide table headers (but not display: none;, for accessibility) */
  thead tr {
    position: absolute;
    top: -9999px;
    left: -9999px;
  }

  tr {
    border: 1px solid #ccc;
  }

  td {
    /* Behave  like a "row" */
    border: none;
    border-bottom: 1px solid #eee;
    position: relative;
    padding-left: 50%;
  }

  td:before {
    /* Now like a table header */
    position: absolute;
    /* Top/left values mimic padding */
    top: 6px;
    left: 6px;
    width: 45%;
    padding-right: 10px;
    white-space: nowrap;
  }

  /*
Label the data
*/
  td:nth-of-type(1):before {
    content: "Period";
  }
  td:nth-of-type(2):before {
    content: "Expected Balance";
  }
  td:nth-of-type(3):before {
    content: "Balance Difference";
  }
  td:nth-of-type(4):before {
    content: "Real Balance";
  }
}
</style>
