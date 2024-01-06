<template>
 <div>

 <p>Username: {{ username }}</p>
 <p>Password: {{ password }}</p>
 <button @click="submit">Submit</button>
 </div>
</template>

<script>
export default {
 props: {
 username: {
  type: String,
  required: true
 },
 password: {
  type: String,
  required: true
 }

 },
 methods: {
 submit() {
 }
 }
}
</script>