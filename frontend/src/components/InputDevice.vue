<template>
 <div>
   <select v-model="selectedDeviceType">
    <option disabled value="">Please select a device type</option>
    <option v-for="deviceType in deviceTypes" :key="deviceType" :value="deviceType">
       {{ deviceType }}
    </option>
   </select>
   <img :src="imagePaths[selectedDeviceType]" alt="Selected Device Image">
 </div>
</template>

<script>
export default {
 data() {
   return {
     selectedDeviceType: '',
     deviceTypes: ['Device Type 1', 'Device Type 2', 'Device Type 3'],// Replace with actual device types
     imagePaths: {
    }
   };
 }
}
</script>