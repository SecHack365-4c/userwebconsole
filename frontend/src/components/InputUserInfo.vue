<!-- components/Input.vue -->
<template>
 <div>
   <form @submit.prevent="submit">
     <label for="devicename">Devicename</label>
     <input type="text" id="devicename" ref="devicename" v-model="devicename">
     <label for="username">Username</label>
     <input type="text" id="username" ref="username" v-model="username">
     <label for="password">Password</label>
     <input type="password" id="password" ref="password" v-model="password">
     <label for='confirm_password'>Confirm Password</label>
     <input type="password" ref="confirmPassword" id="confirm_password" name="confirm_password">
     <button type="submit">Confirm</button>
   </form>
 </div>
</template>
<script>
import axios from 'axios';

export default {
 data() {
  return {
    devicename:'',
    username: '',
    password: ''

  };
 },
 methods: {
  toHalfWidth(str) {
    return str.replace(/[\uff01-\uff5e]/g, function(s) {
      return String.fromCharCode(s.charCodeAt(0) - 0xFEE0);
    }).replace(/[\u3041-\u3096]/g, function(s) {
      return String.fromCharCode(s.charCodeAt(0) + 0x60);
    });
  },
  checkFields() {
    var username = this.toHalfWidth(this.$refs.username.value);
    var password = this.toHalfWidth(this.$refs.password.value);
    var confirmPassword = this.toHalfWidth(this.$refs.confirmPassword.value);

    if (!username || !password || !confirmPassword) {
      alert('Please fill out all fields.');
      return false;
    } else if (password !== confirmPassword) {
      alert('Passwords do not match.');
      return false;
    }

    return true;
  },
  submit() {
    if (this.checkFields()) {
      axios.post('http://your-flask-api-url.com/endpoint', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.error("error",error);
      });
    }
  }
 }
}
</script>