<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <mu-button v-if="!auth" @click="gologin">войти</mu-button>
      <mu-button v-else @click="logout" flat slot="right">выйти</mu-button>
    </mu-appbar>
    <mu-row>
    <Room v-if="auth" @openDialog="openDialog"></Room>
    <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </mu-row>
</mu-container>
</template>

<script>

import Dialog from '@/components/rooms/Dialog'
import Room from '@/components/rooms/Room'


export default {
  name: 'chat',
  
  components: {
    Room,
    Dialog
  },
  
  data(){
   return {
      username: '',
      user_email: '',
      dialog: {
        id: '',
        show: false,
      }
    }
  },
  
  computed: {
    auth(){
      if (sessionStorage.getItem('auth_token')){
        return true
       }
    }
  },
  
  methods: { 
    gologin(){
      this.$router.push({name: "login"})
    },
    logout(){
      sessionStorage.removeItem('auth_token')
      window.location = '/'
    },
    openDialog(id){
      this.dialog.id = id
      this.dialog.show = true
    },

    load() {
      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/fh/dialog/',
        type: 'GET',
        
        data:{
          room: this.id
        },
        
        success: (response) => {
            this.dialogs = response.data.data
        }
      })
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>