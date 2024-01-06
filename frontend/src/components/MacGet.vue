<template>
  <div v-if="macAddresses">
    <button v-for="mac in macAddresses" :key="mac" @click="navigateToMacDetail(mac)">{{ mac }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      macAddresses: ['00:0a:95:9d:68:16', '00:0a:95:9d:68:17', '00:0a:95:9d:68:18'],
      selectedMacAddress: null
    };
  },
  methods: {
    navigateToMacDetail(mac) {
      this.$router.push(`/mac/${mac}`);
    },
    async getMacAddresses() {
      try {
        const response = await axios.get('');
        this.macAddresses = response.data;
      }catch (error) {
        console.error("error", error);
      }
    }
  },
}
</script>