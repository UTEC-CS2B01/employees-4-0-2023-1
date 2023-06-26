<template>
  <div class="home">
    <DepartmentCreation @create-new-department="createDepartment" />
    <DepartmentLists :departments="departments" />
    <EmployeeCreation />
    <EmployeeLists />
  </div>
</template>

<script>
import {
  createDepartment,
  getAllDepartments,
} from "@/services/departments.api";

import DepartmentCreation from "@/components/DepartmentCreation.vue";
import DepartmentLists from "@/components/DepartmentLists.vue";
import EmployeeCreation from "@/components/EmployeeCreation.vue";
import EmployeeLists from "@/components/EmployeeLists.vue";

export default {
  name: "DashboardView",
  components: {
    DepartmentCreation,
    DepartmentLists,
    EmployeeCreation,
    EmployeeLists,
  },
  mounted() {
    this.getDepartments();
  },
  data() {
    return {
      departments: [],
    };
  },
  methods: {
    async getDepartments() {
      const { departments } = await getAllDepartments();
      this.departments = departments;
    },
    async createDepartment(department) {
      const { success, name, short_name } = await createDepartment(department);
      if (success) {
        this.departments.push({ name, short_name });
      }
    },
  },
};
</script>
