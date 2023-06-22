<template>
  <div>
    <h1>List of Employees</h1>
    <ul>
      <li v-for="employee in employees" :key="employee.id">
        {{ employee.firstName }} -- {{ employee.lastName }}
      </li>
    </ul>
  </div>
</template>

<script>
import { getAllEmployees } from "@/services/employees.api";
export default {
  name: "EmployeeList",
  mounted() {
    this.getEmployees();
  },
  data() {
    return {
      employees: [],
    };
  },
  methods: {
    async getEmployees() {
      const { employees } = await getAllEmployees();
      this.employees = employees;
    },
  },
};
</script>

<style></style>
