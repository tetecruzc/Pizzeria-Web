<template> 
  <div style="display:flex;align-items:center;justify-content:center;width:100%;">
     <div v-if="!bill && !drinksSection" class="container">
       <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>Escoja los ingredientes de la pizza # {{ number }}</h1>

        <p class="subtitle">Tamaño: </p>
        <b-form-select v-model="selectedSize" :options="sizes" style="font-size:20px"></b-form-select>
        <p class="subtitle">Ingredientes:</p>
        <div class="container-dark">
            <!-- <b-form-radio  style="font-size:20px"  v-for="(ingredient,index) in ingredients" :key="index" v-model="ingredients[index].selected" :aria-describedby="ariaDescribedby"  :value="ingredient.id">{{ingredient.name}}</b-form-radio> -->
            <b-form-group  v-slot="{ ariaDescribedby }" style="font-size: 20px;">
                  <b-form-checkbox-group
                    id="checkbox-group-2"
                    v-model="selectedIngredients"
                    :aria-describedby="ariaDescribedby"
                    name="flavour-2"
                    style="font-size: 20px;"
                  >
                    <b-form-checkbox  v-for="(ingredient,index) in ingredients" :key="index" :value="ingredient.id">{{ingredient.name}} ($ {{ingredient.price}})</b-form-checkbox>
                  
                  </b-form-checkbox-group>
            </b-form-group>
        </div>
        <b-alert v-model="notFountSizeAlert" style="font-size: 20px;" variant="danger" dismissible>
          Debe seleccionar un tamaño para su pizza!
        </b-alert>
        <b-button
            variant="primary"
            class="float-right custom-button-primary"
            @click="showDrinks()"
             
          >
            Siguiente
          </b-button>
   </div>
    <div v-if="!bill && drinksSection" class="container">
       <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>Bebidas de la pizza # {{ number }}</h1>

        <p class="subtitle">Bebidas:</p>
        <div class="container-dark">
            <!-- <b-form-radio  style="font-size:20px"  v-for="(ingredient,index) in ingredients" :key="index" v-model="ingredients[index].selected" :aria-describedby="ariaDescribedby"  :value="ingredient.id">{{ingredient.name}}</b-form-radio> -->
            <b-form-group style="font-size: 20px;"  v-slot="{ ariaDescribedbyy }">
              <b-form-radio v-model="selectedDrink" :aria-describedby="ariaDescribedbyy"  v-for="(drink,index) in drinks" :key="index" :value="drink.id">{{drink.name}} ($ {{drink.price}})</b-form-radio>
          </b-form-group>
        </div>
        <b-modal
          v-model="modalShow"
          title="Continuar orden ..."

        >
      <b-container fluid style="font-size: 20px;">
        <p>Usted ha ordenado una pizza tamaño {{selectedSizeName}}</p>
        <p> Desea usted ordenar alguna otra pizza planeta?</p>
      </b-container>

      <template #modal-footer>

          <b-button
            variant="primary"
            
            class=" custom-button-secondary"
            @click="showBill()"
          >
            Finalizar orden
          </b-button>
         <b-button
            variant="primary"
            
            class=" custom-button-secondary"
            @click="getAnotherPizza()"
          >
            Si, quiero otra pizza
          </b-button>

      </template>
    </b-modal>
        <b-button
            variant="primary"
            class="float-right custom-button-primary"
            @click="openModal()"
             
          >
            Siguiente
          </b-button>
   </div>
   <div v-if="bill" class="container">
         <svg class="topIcon" viewBox="0 0 40 40" role="img">
            <path d="M20 9c7.18 0 13 5.82 13 13 0 7.077-5.655 12.833-12.693 12.996L20 35H0v-2h20c6.075 0 11-4.925 11-11s-4.925-11-11-11c-5.979 0-10.843 4.77-10.996 10.712L9 22H7c0-7.18 5.82-13 13-13zM9 29v2H2.96v-2H9zm0-4v2H5.98v-2H9zm17.244-8.635l1.312 1.51-7.8 6.78-1.312-1.51 7.8-6.78zm6.132-5.98l1.93 2.23-1.512 1.31-1.93-2.23 1.512-1.31zM24.5 5v2h-9V5h9z">
            </path>
        </svg>
        <h1>Factura Pizza planeta</h1>
        <b-table striped hover :items="items" style="font-size: 20px;"></b-table>
          <b-alert style="font-size:20px;" variant="success" show v-model="confirmModal">Su pedido ha sido registrado exitosamente</b-alert>
          <b-alert style="font-size:20px;" show variant="danger" v-model="errorModal">Ha ocurrido un error registrando su pedido</b-alert>
           <b-button
            variant="primary"
            class="float-right custom-button-primary"
            @click="saveOrder()"
             
          >
            Confirmar compra
          </b-button>

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
      selectedIngredients: [],
      selectedDrink: '',
      modalShow: false,
      drinksSection: false,
      sizes : [],
      ingredients: [],
      drinks: [],
     // sizes: [{value:1,text:'Personal', price: 10.00},{value:2,text:'Mediana', price: 16.0},{value:3,text:'Grande', price: 20.0}],
     // ingredients: [{id:1,name:'Pepperoni',selected:'', price : 3.85},{ id:2,name:'Jamón',selected:'', price: 4.0},{ id:3,name:'Champiñones',selected:'', price: 3.5},{ id:4,name:'Pimentón',selected:'', price: 3.0},{ id:5,name:'Doble Queso',selected:'', price: 4.0},{ id:6,name:'Aceitunas',selected:'', price: 5.75},{ id:7,name:'Salchichón',selected:'', price: 62.5}],
     // drinks: [{id:1,name:'Cocacola',price:1.7},{id:2,name: 'Pepsicola',price:1.8},{id:3,name: 'Frescolita',price:2.0}],
      selectedSize: null,
      pizzas: [],
      orderId: null,
      userId : null,
      bill: false,
      notFountSizeAlert: false,
      confirmModal: false,
      errorModal: false,
      pizzaPrice: 0,
      totalPrice: 0
     }
  },
  created(){
        this.getSizes();
        this.getIngredients();
        this.getDrinks();
        this.getOrderId();
        this.userId = parseInt(this.$router.history.current.params.id)
  },
  methods:{
     showDrinks(){
          if (this.selectedSize !== null){
                  this.drinksSection = true;
                   this.notFountSizeAlert = false
          }
          else{
                  this.notFountSizeAlert = true
          }  
       
     },
     saveOrder(){
         const path = 'http://127.0.0.1:8000/create-pizza';
          axios.post(path,this.pizzas)
          .then((response)=>{
              this.errormodal = false
              this.confirmModal = true
            })
          .catch((error)=>{
               console.log(error)
                this.confirmModal = false
               this.errormodal = true
          })        
     },
     getDrinks(){
           const path = 'http://127.0.0.1:8000/get-drinks';
            axios.get(path).then((response)=>{
                this.drinks = response.data
            })
          .catch((error)=>{
               console.log(error)
          })
     },
     getSizes(){
         var sizes = []
         const path = 'http://127.0.0.1:8000/get-sizes';
            axios.get(path).then((response)=>{
                sizes = response.data
                for (var i=0; i<sizes.length;i++){
                   this.sizes.push({value: sizes[i].id, text: sizes[i].name, price: sizes[i].price}) 
                }
            })
          .catch((error)=>{
               console.log(error)
          })
     },
     getIngredients(){
         const path = 'http://127.0.0.1:8000/get-ingredients';
            axios.get(path).then((response)=>{
                this.ingredients = response.data
            })
          .catch((error)=>{
               console.log(error)
          })
     },
     savePizza(){
        for (var j=0; j<this.selectedIngredients.length;j++){
          this.pizzaPrice = this.pizzaPrice + parseFloat(this.getIngredientPrice(this.selectedIngredients[j]))
        }
        this.pizzaPrice = this.pizzaPrice + parseFloat(this.getSizePrice(this.selectedSize))
        if (this.selectedDrink !== ""){
              this.pizzaPrice = this.pizzaPrice + parseFloat(this.getDrinkPrice(this.selectedDrink))
        }
        this.modalShow=false;
        this.pizzas.push({user:this.userId,size:this.selectedSize,ingedients:this.selectedIngredients,orderId:this.orderId, totalPrice: this.pizzaPrice, drink: this.selectedDrink})
        this.totalPrice = this.totalPrice + this.pizzaPrice;
        this.pizzaPrice = 0
        this.selectedIngredients = []
     },
     getOrderId(){
        const path = 'http://127.0.0.1:8000/last-order';
            axios.get(path).then((response)=>{
                this.orderId  = response.data.orderId + 1
                console.log(this.orderId)
            })
          .catch((error)=>{
               console.log(error)
          })
     },
      showBill(){        
        this.savePizza()
        this.bill = true
       // this.goToUrl('OrderResult',this.userId)
      },
      getAnotherPizza(){
        this.bill = false;
        this.drinksSection = false;
        this.savePizza();
        this.selectedSize = null;
        this.selectedDrink = '';
        this.number ++; 
        for (var i=0; i<this.ingredients.length;i++){
    
          if (this.ingredients[i].selected !== ''){
              this.ingredients[i].selected = ''
          }
        }
      },
     goToUrl(url, id) {
        this.$router.push({
            name: url,
            params: { id: id },
          })
          .catch(() => {});
      },
      getSizeName(id){
          for (var i=0; i<this.sizes.length;i++){
            if (this.sizes[i].value === id){
              return this.sizes[i].text
            }   
          }
          return null
      },
      getDrinkName(id){
          for (var i=0; i<this.drinks.length;i++){
            if (this.drinks[i].id === id){
              return this.drinks[i].name
            }   
          }
          return null
      },
      getIngredientName(id){
          for (var i=0; i<this.ingredients.length;i++){
            if (this.ingredients[i].id === id){
                return this.ingredients[i].name
            }
          }
          return null
      },
      getSizePrice(id){
          for (var i=0; i<this.sizes.length;i++){
            if (this.sizes[i].value === id){
                return this.sizes[i].price
            }
          }
          return null
      },
      getDrinkPrice(id){
          for (var i=0; i<this.drinks.length;i++){
            if (this.drinks[i].id === id){
                return this.drinks[i].price
            }
          }
          return null
      },
      getIngredientPrice(id){
          for (var i=0; i<this.ingredients.length;i++){
            if (this.ingredients[i].id === id){
                return this.ingredients[i].price
            }
          }
          return null
      },
       getPizzaPrice(){
         
      },
      openModal(){
            this.modalShow= true;  
                  
      },

  },
  computed:{
      selectedSizeName:{
          get: function(){
              var name = null
              for (var i=0; i<this.sizes.length;i++){
                if (this.sizes[i].value === this.selectedSize){    
                    name = this.sizes[i].text
                }
              }
              return name;
          }
    },
    items:{
        get: function(){
            var number = 1;
            var ingredients = "";
            var size = ""
            var items = []
            var price = 0
            var drink = ""
            var accumPrice = 0
            for (var i=0; i<this.pizzas.length;i++){
                for (var j=0; j<this.pizzas[i].ingedients.length;j++){
                  if (j === (this.pizzas[i].ingedients.length -1)){
                    ingredients = ingredients + '' +this.getIngredientName(this.pizzas[i].ingedients[j])
                  }
                  else{
                    ingredients = this.getIngredientName(this.pizzas[i].ingedients[j])+ " , " + ingredients 
                  }
                  price = price + parseFloat(this.getIngredientPrice(this.pizzas[i].ingedients[j]))
                  
                }
                size = this.getSizeName(this.pizzas[i].size)
                price = price + parseFloat(this.getSizePrice(this.pizzas[i].size))
                if (this.pizzas[i].drink !== ""){
                      price = price + parseFloat(this.getDrinkPrice(this.pizzas[i].drink))
                      drink = this.getDrinkName(this.pizzas[i].drink)
                      
                }
                price = price.toFixed(2);
                items.push({Numero : number, Ingredientes: ingredients, Tamaño: size, Bebida: drink, Precio: '$ '+price})
                number++;
                ingredients = "";
                accumPrice = (parseFloat(accumPrice) + parseFloat(price)).toFixed(2);
                price  = 0;
            }
            items.push({Bebida: 'Total: ', Precio: '$ '+accumPrice})
            return items
        }
    }
  }
  
   
}
</script>

<style scoped>

</style>
