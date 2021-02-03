<template> 
   <div class="container">
        <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>{{ title }}</h1>
        <div class="input-container">
            <input class="input" type="text" v-model="name"  placeholder="Nombre">
        </div>
        <div class="input-container">
            <input class="input" type="text" v-model="lastname" placeholder="Apellido">
        </div>
        <div class="input-container">
            <input class="input" type="date" v-model="birthday" placeholder="Fecha de nacimiento">
        </div>
        <b-alert v-model="notFountField" style="font-size: 20px;" variant="danger" dismissible>
          Debe ingresar todos los campos!
        </b-alert>
         <b-button
            variant="primary"
            class="float-right custom-button-primary"
             @click="createUser('OrderPizzas')"
             
          >
            Siguiente
          </b-button>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UserData',
  data () {
    return {
      title: 'Ingrese sus datos para proseguir con la orden',
      name: '',
      lastname: '',
      birthday: '',
      notFountField: false
     }
  },
  methods:{
    createUser(url) {
        if ( this.name === '' || this.lastname === '' || this.birthday === ''){
            this.notFountField = true
        }
        else{       
             this.notFountField = false
            const path = 'http://127.0.0.1:8000/create-user';
            axios.post(path,{
                id: this.$router.history.current.params.id,
                name: this.name,
                lastname: this.lastname,
                birthday: this.birthday
                
            }).then((response)=>{
                console.log(response.data)
                this.$router.push({
                    name: url
                })
                .catch(() => {});

            })
          .catch((error)=>{
               console.log(error)
          })        
        }
    }
  },
   
}
</script>

<style scoped>

</style>