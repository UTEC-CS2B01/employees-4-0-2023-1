<template>
  <div class="app-container">
    <div class="menu">
      <TheNavigation />
    </div>
    <div class="portal">
      <router-view />
    </div>
  </div>
</template>

<script>
import TheNavigation from "@/views/TheNavigation.vue";
export default {
  name: "App",
  components: {
    TheNavigation,
  },
};
</script>

<style>
.app-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}

.menu {
  flex: 0 0 30%; /* Adjust the width as needed */
  background-color: transparent;
}

.portal {
  flex: 1;
}
</style>
