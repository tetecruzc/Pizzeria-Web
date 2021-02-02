<template> 
   <div class="container">
       <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>{{ title }}</h1>
       <b-table striped hover :items="items"></b-table>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'OrderResult',
  data () {
    return {
      title: 'Factura Pizza planeta',
      items: [
          { Numero: 1, Tamaño: 'Pequeña', Ingredientes: 'Pimentón,Pepperoni' , price: 32.12},
          { Numero: 2, Tamaño: 'Pequeña', Ingredientes: 'Jamon,Salchichon' , price: 32.12},
          { Numero: 3, Tamaño: 'Pequeña', Ingredientes: 'Jamon' , price: 32.12},
          { Numero: 4, Tamaño: 'Pequeña', Ingredientes: 'Champiñones' , price: 32.12},
          {Ingredientes: 'Total: ',price: 128.48}
        ]
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
  },
   
}
</script>

<style scoped>

</style>
