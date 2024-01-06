<template>
  <div class="home">
    <MacAddress/>
  </div>
</template>

<script>
// @ is an alias to /src

import MacAddress from '../components/MacGet.vue'


export default {
  name: 'HomeView',
  components: {
    MacAddress
  }
}
</script>
