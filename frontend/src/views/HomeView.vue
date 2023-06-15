<template>
  <div class="home">
    <h1>Dashboard</h1>
    <DepartmentCreation />
  </div>
</template>

<script>
import DepartmentCreation from "@/components/DepartmentCreation.vue";
export default {
  name: "HomeView",
  components: {
    DepartmentCreation,
  },
};
</script>
