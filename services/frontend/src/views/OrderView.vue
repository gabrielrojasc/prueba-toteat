<template>
  <div class="container-fluid">
    <div class="row m-3 px-5">
      <div class="col me-auto">
        <h3 class="text-start">Order details</h3>
      </div>
      <div class="col-auto">
        <router-link :to="{ name: 'Orders' }" class="btn btn-dark"
          >Go Back</router-link
        >
      </div>
    </div>
    <div class="row mx-5 px-5 text-start">
      <p>
        <span class="fw-bold">Date Opened</span>:
        {{ formatDate(order.date_opened) }}
      </p>
      <p>
        <span class="fw-bold">Date Closed</span>:
        {{ formatDate(order.date_closed) }}
      </p>
      <p><span class="fw-bold">Zone</span>: {{ order.zone }}</p>
      <p><span class="fw-bold">Table</span>: {{ order.table }}</p>
      <p><span class="fw-bold">Diners</span>: {{ order.diners }}</p>
      <p><span class="fw-bold">Waiter</span>: {{ order.waiter }}</p>
      <p><span class="fw-bold">Cashier</span>: {{ order.cashier }}</p>
      <div class="row">
        <div class="col">
          <p><span class="fw-bold">Products</span>:</p>
          <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Name</th>
                  <th scope="col">Category</th>
                  <th scope="col">Price</th>
                  <th scope="col">Quantity</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in order.products">
                  <td>{{ product.name }}</td>
                  <td>{{ product.category }}</td>
                  <td>{{ formatMoney(product.price) }}</td>
                  <td>{{ product.quantity }}</td>
                </tr>
              </tbody>
              <tfoot>
                <tr>
                  <td colspan="2"></td>
                  <td>Sum:</td>
                  <td v-if="order">{{ formatMoney(productSum) }}</td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
        <div class="col">
          <p><span class="fw-bold">Payments</span>:</p>
          <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Type</th>
                  <th scope="col">Amount</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="payment in order.payments">
                  <td>{{ payment.type }}</td>
                  <td>{{ formatMoney(payment.amount) }}</td>
                </tr>
              </tbody>
              <tfoot>
                <tr>
                  <td>Total:</td>
                  <td>{{ formatMoney(order.total) }}</td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      </div>
    </div>
    <br />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderView",
  data() {
    return {
      order: {},
      productSum: 0,
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
      return dateObj.toDateString();
    },
    async fetchOrder(order_id) {
      const res = await axios.get(`/order/${order_id}`);
      const data = res.data;
      return data;
    },
  },
  async created() {
    const order_id = this.$route.params.id;
    this.order = await this.fetchOrder(order_id);
    this.productSum = this.order.products.reduce(
      (prev, curr) => prev + curr.price * curr.quantity,
      0
    );
  },
};
</script>
