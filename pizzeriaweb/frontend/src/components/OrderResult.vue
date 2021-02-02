<template> 
   <div class="container">
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
