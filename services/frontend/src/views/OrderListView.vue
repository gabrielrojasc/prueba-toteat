<template>
  <div class="container-fluid mt-4">
    <h1>Orders</h1>
    <br />
    <div class="row">
      <div class="col-1"></div>
      <div class="col-10">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Table</th>
              <th scope="col">Diners</th>
              <th scope="col">Balance Difference</th>
              <th scope="col">Total</th>
              <th scope="col">Date</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody v-if="loaded">
            <tr v-for="(order, index) in orders">
              <th scope="row">{{ index + firstId }}</th>
              <td>{{ order.table }}</td>
              <td>{{ order.diners }}</td>
              <td>{{ formatMoney(order.total - sumProducts(order)) }}</td>
              <td class="text-align-left">{{ formatMoney(order.total) }}</td>
              <td>{{ formatDate(order.date_opened) }}</td>
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
      </div>
    </div>
    <nav aria-label="Page navigation">
      <ul class="pagination pagination-dark justify-content-center">
        <li :class="{ disabled: !loaded || !hasPrev }" class="page-item">
          <a @click="prevPage" class="page-link">Previous</a>
        </li>
        <li class="page-item">
          <p class="page-link page-text">
            {{ firstId }}-{{ firstId + orders.length - 1 }}
          </p>
        </li>
        <li :class="{ disabled: !loaded || !hasNext }" class="page-item">
          <a @click="nextPage" class="page-link">Next</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderListView",
  data() {
    return {
      orders: [],
      firstId: 1,
      currentPage: 1,
      hasPrev: false,
      hasNext: false,
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
      return dateObj.toDateString();
    },
    async fetchData(page) {
      const res = await axios.get(`/orders?page=${page}`);
      const data = res.data;
      return data;
    },
    async nextPage() {
      this.loaded = false;
      this.currentPage++;
      const data = await this.fetchData(this.currentPage);
      this.setData(data);
    },
    async prevPage() {
      this.loaded = false;
      this.currentPage--;
      const data = await this.fetchData(this.currentPage);
      this.setData(data);
    },
    sumProducts(order) {
      return order.products.reduce(
        (prev, curr) => prev + curr.price * curr.quantity,
        0
      );
    },
    setData(data) {
      this.orders = data.items;
      this.currentPage = data.page;
      this.firstId = 1 + (this.currentPage - 1) * 50;
      this.hasNext = this.currentPage < this.totalPages;
      this.hasPrev = this.currentPage > 1;
      this.loaded = true;
    },
  },
  async created() {
    const data = await this.fetchData(this.currentPage);
    this.totalPages = Math.ceil(data.total / data.size);
    this.setData(data);
  },
};
</script>

<style scoped>
.page-link:hover {
  cursor: pointer;
}
.page-text {
  color: black;
}
.page-text:hover {
  color: black;
  background: white;
  cursor: auto;
}
</style>

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
    content: "Table";
  }
  td:nth-of-type(2):before {
    content: "Diners";
  }
  td:nth-of-type(3):before {
    content: "Balance Difference";
  }
  td:nth-of-type(4):before {
    content: "Total";
  }
  td:nth-of-type(5):before {
    content: "Date";
  }
}
</style>
