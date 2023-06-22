<template>
  <div class="home">
    <DepartmentCreation />
    <DepartmentLists />
  </div>
</template>

<script>
import DepartmentCreation from "@/components/DepartmentCreation.vue";
import DepartmentLists from "@/components/DepartmentLists.vue";
export default {
  name: "HomeView",
  components: {
    DepartmentCreation,
    DepartmentLists,
  },
};
</script>
