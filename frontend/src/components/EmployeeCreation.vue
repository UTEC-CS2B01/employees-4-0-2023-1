<template>
  <div>
    <h1>Create Employee:</h1>
    <form @submit.prevent="createEmployeeEvent">
      <div class="form-group">
        <label>First Name:</label>
        <input type="text" v-model.trim="employee.firstName" />
      </div>
      <div class="form-group">
        <label>Last Name:</label>
        <input type="text" v-model.trim="employee.lastName" />
      </div>
      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
import { createEmployee } from "@/services/employees.api";
export default {
  name: "EmployeeCreation",
  data() {
    return {
      employee: {
        firstName: "",
        lastName: "",
      },
    };
  },
  methods: {
    async createEmployeeEvent() {
      const response = await createEmployee(this.employee);
      console.log("response = ", response);
    },
  },
};
</script>

<style>
.form-group {
  margin-bottom: 1rem;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 300px;
}

label {
  display: block;
  margin-bottom: 5px;
}

.submit-button {
  background-color: green;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
