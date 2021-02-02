<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
   <b-table striped hover :items="pizzas" :fields="fields">

   </b-table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Bienvenido ',
      pizzas: [],
      fields:[
        {key: 'X', label: 'x'},
        {key: 'Y', label: 'y'}
      ]
    }
  },
  methods:{
    getPizzas(){
      const path = 'http://127.0.0.1:8000/api/v1.0/pizzas'
      axios.get(path).then((response)=>{
        this.pizzas = response.data
      })
      .catch((error)=>{
        console.log(error)
      })
    }
  },
    created(){
    this.getPizzas()
    console.log(this.pizzas)
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
