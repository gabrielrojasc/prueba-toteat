<template>
  <div class="container-fluid py-3 px-5">
    <div class="row m-3">
      <div class="col-9">
        <h3 class="text-start">Order details</h3>
      </div>
      <div class="col-3">
        <router-link :to="{ name: 'Orders' }" class="btn btn-dark"
          >Go Back</router-link
        >
      </div>
    </div>
    <div class="row mx-5 text-start">
      <p><span class="fw-bold">Date Opened</span>: {{ order.date_opened }}</p>
      <p><span class="fw-bold">Date Closed</span>: {{ order.date_closed }}</p>
      <p><span class="fw-bold">Zone</span>: {{ order.zone }}</p>
      <p><span class="fw-bold">Table</span>: {{ order.table }}</p>
      <p><span class="fw-bold">Diners</span>: {{ order.diners }}</p>
      <p><span class="fw-bold">Waiter</span>: {{ order.waiter }}</p>
      <p><span class="fw-bold">Cashier</span>: {{ order.cashier }}</p>
      <p><span class="fw-bold">Total</span>: {{ order.total }}</p>
      <p><span class="fw-bold">Products</span>:</p>
      <div class="row">
        <div class="col-1"></div>
        <div class="col-6">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Category</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
              </tr>
            </thead>
            <tbody v-for="product in order.products">
              <tr>
                <td>{{ product.name }}</td>
                <td>{{ product.category }}</td>
                <td>{{ product.price }}</td>
                <td>{{ product.quantity }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <p><span class="fw-bold">Payments</span>:</p>
      <div class="row">
        <div class="col-1"></div>
        <div class="col-6">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Type</th>
                <th scope="col">Amount</th>
              </tr>
            </thead>
            <tbody v-for="payment in order.payments">
              <tr>
                <td>{{ payment.type }}</td>
                <td>{{ payment.amount }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <br />
  </div>
  {{ currentPage }}
</template>

<script>
import axios from "axios";

export default {
  name: "OrderView",
  data() {
    return {
      order: {},
    };
  },
  methods: {
    async fetchOrder(order_id) {
      const res = await axios.get(`/order/${order_id}`);
      const data = res.data;
      return data;
    },
  },
  async created() {
    const order_id = this.$route.params.id;
    this.order = await this.fetchOrder(order_id);
  },
};
</script>
