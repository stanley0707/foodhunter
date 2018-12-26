<template>
  <mu-col span="8" xl="10">
    
    <mu-container class="dialog">
    <mu-row direction="column" 
        justify-content="start"
        align-item="end" 
        v-for="dialog in dialogs">
        <p> <strong>{{ dialog.user.first_name }}</strong></p>
        <p>{{ dialog.text }}</p>
        <span>{{ dialog.date }}</span>
    </mu-row>
    </mu-container>
    <mu-container>
      <mu-row align-item="round">
        <mu-text-field 
          multi-line :rows="6" 
          v-model="form.textarea"
          full-width
          placeholder="сообщение">
        </mu-text-field>
        <mu-button class="btn-send" round color="success" @click="sendMessage">отправить</mu-button>
      </mu-row>
    </mu-container>
   </mu-col>
</template>

<script>
//import io from 'socket.io-client';

export default {

  name: 'Dialog',
  
  props: {
    id: ''
  },
  
  data() {
    return {
      dialogs: '',
      form: {
        textarea: '',
      },
      //socket : io('localhost:4000'),
      //socket,
      msgObject: {} 
    }
  },
 
  created() {
    $.ajaxSetup({
      headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
    });

    this.loadDialog()
    //setInterval(() => {
        this.loadDialog()
    //}, 1500)
  },
  
  methods: {

    loadDialog() {
      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/fh/dialog/',
        type: 'GET',
        
        data:{
          room: this.id
        },
        
        success: (response) => {
            this.dialogs = response.data.data
            console.log(response.data.data)
        }
      })
    },
    
    sendMessage() {
      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/fh/dialog/',
        type: 'POST',
        
        data:{
          room: this.id,
          text: this.form.textarea
        },
        
        success: (response) => {
            this.loadDialog()
        },

        //error: (response) => {
        //  alert(response.statusText)
        // }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.dialog{
  border: 1px solid #000
}
.btn-send{
  padding: 10px;
}
</style>