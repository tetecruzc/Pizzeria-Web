<template> 
   <div class="container">
        <h1>Escoja los ingredientes de la pizza Nro{{ number }}</h1>
       <b-dropdown text="Outline Primary" variant="outline-primary" class="m-2">
            <b-dropdown-item href="#">Action</b-dropdown-item>
            <b-dropdown-item href="#">Another action</b-dropdown-item>
            <b-dropdown-item href="#">Something else here</b-dropdown-item>
        </b-dropdown>
         <b-form-group label="Individual radios" v-slot="{ ariaDescribedby }">
        <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="A">Option A</b-form-radio>
        <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="B">Option B</b-form-radio>
        </b-form-group>

        <b-modal
      v-model="modalShow"
      title="Continuar orden ..."
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <b-container fluid>
       Desea usted ordenar alguna otra pizza planeta?
      </b-container>

      <template #modal-footer>

          <b-button
            variant="primary"
            size="sm"
            class="float-right"
            @click="modalShow=false"
          >
            Finalizar orden
          </b-button>
         <b-button
            variant="primary"
            size="sm"
            class="float-right"
            @click="modalShow=false"
          >
            Continuar
          </b-button>

      </template>
    </b-modal>
    <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
        <div class="button" @click="openModal()">
            <input class="button-submit" type="submit" value="Siguiente" >
            <svg class="button-icon" role="img" viewBox="0 0 24 24"><path d="M15.49 21.48a1 1 0 01-1.54 0 1.19 1.19 0 010-1.63l6.33-6.71H1.09a1.15 1.15 0 010-2.3h19.17L14 4.15a1.19 1.19 0 010-1.63 1 1 0 011.54 0l8.19 8.66a1.21 1.21 0 010 1.64z" ></path></svg>
        </div>
   </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'OrderPizzas',
  data () {
    return {
      number: 1,
      selected: '',
      modalShow: false
     }
  },
  methods:{
     goToUrl(url, id) {
        this.$router.push({
            name: url,
            params: { id: id },
          })
          .catch(() => {});
      },
      openModal(){
          this.modalShow= true;
          this.goToUrl('OrderPizzas')
      }
  },
   
}
</script>

<style scoped>

</style>
