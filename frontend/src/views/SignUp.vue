<template>
  <div>
    <form @submit.prevent.stop="signUpEvent">
      <div class="form-group">
        <label>Username:</label>
        <input type="text" v-model.trim="username" />
      </div>
      <div class="form-group">
        <label>Password:</label>
        <input type="password" v-model.trim="password" />
      </div>
      <div class="form-group">
        <label>Confirm Password:</label>
        <input type="password" v-model.trim="confirmationPassword" />
      </div>
      <button class="submit-button">Sign Up</button>
    </form>
  </div>
</template>

<script>
import { signUp } from "@/services/users.api";
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      confirmationPassword: "",
    };
  },
  methods: {
    async signUpEvent() {
      const response = await signUp({
        username: this.username,
        password: this.password,
        confirmationPassword: this.confirmationPassword,
      });
      console.log("response: ", response);
    },
  },
};
</script>

<style>
.form-group {
  margin-bottom: 1rem;
}

input[type="text"],
input[type="password"],
button {
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
