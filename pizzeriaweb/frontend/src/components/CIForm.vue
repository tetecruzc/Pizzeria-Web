<template> 
   <div class="container">
        <h1>{{ title }}</h1>
         <div class="input-container">
            <input class="input" type="number" name="ci" placeholder="CI">
        </div>
        <div class="button" @click="goToUrl('UserData',1)">
            <input class="button-submit" type="submit" value="Siguiente">
            <svg class="button-icon" role="img" viewBox="0 0 24 24"><path d="M15.49 21.48a1 1 0 01-1.54 0 1.19 1.19 0 010-1.63l6.33-6.71H1.09a1.15 1.15 0 010-2.3h19.17L14 4.15a1.19 1.19 0 010-1.63 1 1 0 011.54 0l8.19 8.66a1.21 1.21 0 010 1.64z" ></path></svg>
        </div>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CIForm',
  data () {
    return {
      title: 'Ingrese su CI para iniciar la orden',
     }
  },
  methods:{
     goToUrl(url, id) {
        this.$router.push({
            name: url,
            params: { id: id },
          })
          .catch(() => {});
      }
  }
   
}
</script>

<style scoped>

</style>
