<template>
  <div class="home">
    <DepartmentCreation />
    <DepartmentLists />
    <EmployeeCreation />
    <EmployeeLists />
  </div>
</template>

<script>
import DepartmentCreation from "@/components/DepartmentCreation.vue";
import DepartmentLists from "@/components/DepartmentLists.vue";
import EmployeeCreation from "@/components/EmployeeCreation.vue";
import EmployeeLists from "@/components/EmployeeLists.vue";

export default {
  name: "HomeView",
  components: {
    DepartmentCreation,
    DepartmentLists,
    EmployeeCreation,
    EmployeeLists,
  },
};
</script>
