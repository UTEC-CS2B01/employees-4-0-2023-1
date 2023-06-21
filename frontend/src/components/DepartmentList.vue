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
export default {
  name: "DepartmentList",
  data() {
    return {
      departments: [],
    };
  },
};
</script>

<style></style>
