<template>
  <div>
    <h1>List of Departments</h1>
    <ul>
      <li v-for="dpto in departments" :key="dpto.id">
        {{ dpto.name }} -- {{ dpto.short_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { getAllDepartments } from "@/services/departments.api";
export default {
  name: "DepartmentLists",
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
  },
};
</script>

<style></style>
