<template> 
   <div class="container">
       <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
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
