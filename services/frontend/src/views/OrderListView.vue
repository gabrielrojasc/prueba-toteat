<template>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Id</th>
        <th scope="col">Table</th>
        <th scope="col">Diners</th>
        <th scope="col">Number of products</th>
        <th scope="col">Total</th>
        <th scope="col">Date</th>
        <th scope="col"></th>
      </tr>
    </thead>
    <tbody v-for="(order, index) in orders">
      <tr>
        <th scope="row">{{ index + 1 }}</th>
        <td>{{ order.table }}</td>
        <td>{{ order.diners }}</td>
        <td>{{ order.products.length }}</td>
        <td class="text-align-left">${{ order.total }}</td>
        <td>{{ order.date_opened }}</td>
        <td>
          <router-link
            :to="{ name: 'Order', params: { id: order.id } }"
            class="btn btn-dark"
            >Detail</router-link
          >
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderListView",
  data() {
    return {
      orders: [],
    };
  },
  methods: {
    async fetchOrders() {
      const res = await axios.get("/orders");
      const data = res.data;
      return data;
    },
  },
  async created() {
    this.orders = await this.fetchOrders();
  },
};
</script>
