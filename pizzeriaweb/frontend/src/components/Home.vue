<template> 
   <div class="container">
        <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>{{ title }}</h1>
        <h2>{{ subtitle }}</h2>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  data () {
    return {
      title: 'Bienvenido a PizzaPlaneta',
      subtitle: 'Ordena tu pizza ya!',
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
