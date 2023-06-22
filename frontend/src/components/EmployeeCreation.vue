<template>
  <div>
    <h1>Create Employee:</h1>
    <form @submit.prevent.stop="createEmployeeEvent">
      <div class="form-group">
        <label>First Name:</label>
        <input type="text" v-model="employee.first_name" />
      </div>
      <div class="form-group">
        <label>Last Name:</label>
        <input type="text" v-model="employee.last_name" />
      </div>
      <div class="form-group">
        <label>Job Title:</label>
        <input type="text" v-model="employee.job_title" />
      </div>
      <div class="form-group">
        <select v-model="employee.selectDepartment">
          <option
            v-for="department in departments"
            :key="department.id"
            :value="department.id"
          >
            {{ department.name }}
          </option>
        </select>
      </div>
      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
import { createEmployee } from "@/services/employees.api";
import { getAllDepartments } from "@/services/departments.api";
export default {
  name: "EmployeeCreation",
  async mounted() {
    await this.loadDepartments();
  },
  data() {
    return {
      employee: {
        first_name: "",
        last_name: "",
        job_title: "",
        selectDepartment: null,
      },
      departments: [],
    };
  },
  methods: {
    async loadDepartments() {
      const { departments } = await getAllDepartments();
      this.departments = departments;
    },
    async createEmployeeEvent() {
      const data = await createEmployee(this.employee);
      console.log("data: ", data);
    },
  },
};
</script>

<style>
.form-group {
  margin-bottom: 1rem;
}

input[type="text"],
select {
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
