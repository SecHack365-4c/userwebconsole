<template>
  <div class="home">
    <InputDevice/>
    <InputUser/>
    <InputCheck/>
  </div>
</template>

<script>
// @ is an alias to /src

import InputUser from '../components/InputUserInfo.vue'
import InputDevice from  '../components/InputDevice.vue'
import InputCheck from '../components/InputCheck.vue'

export default {
  name: 'HomeView',
  components: {
    InputUser,
    InputDevice,
    InputCheck
  }
}
</script>
