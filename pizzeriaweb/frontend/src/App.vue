<template>
  <div id="app">
    <left-menu />
    <router-view/>
  </div>
</template>

<script>
import leftMenu from "@/components/layout/leftMenu.vue"
export default {
  name: 'App',
  data(){

  },
  components:{
      leftMenu
  },
  methods:{

  }
}
</script>

<style >
 @import './styles/main.css';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  display: flex;
  width: 100vw;
}
</style>