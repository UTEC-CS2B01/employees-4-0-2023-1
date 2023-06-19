<template>
  <div class="home">
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
