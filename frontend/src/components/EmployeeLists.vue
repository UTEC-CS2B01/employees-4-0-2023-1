<template>
  <div>
    <h1>List of Employees</h1>
    <ul>
      <li v-for="employee in employees" :key="employee.id">
        {{ employee.first_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { getAllEmployees } from "@/services/employees.api";
export default {
  name: "EmployeeLists",
  mounted() {
    this.loadEmployees();
  },
  data() {
    return {
      employees: [],
    };
  },
  methods: {
    async loadEmployees() {
      const { employees } = await getAllEmployees();
      this.employees = employees;
    },
  },
};
</script>

<style></style>
