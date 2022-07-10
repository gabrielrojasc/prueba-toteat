<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1">La Pikada de la Esquina</span>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <router-link
            :to="{ name: 'Dashboard' }"
            class="nav-link"
            :class="{ active: routeName === 'Dashboard' ? true : false }"
            >Dashboard</router-link
          >
          <router-link
            :to="{ name: 'Orders' }"
            class="nav-link"
            :class="{
              active:
                routeName === 'Orders' || routeName === 'Order' ? true : false,
            }"
            >Orders</router-link
          >
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  computed: {
    routeName() {
      return this.$route.name;
    },
  },
};
</script>
