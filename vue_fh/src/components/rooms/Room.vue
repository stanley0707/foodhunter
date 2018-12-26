<template>
  <mu-col span="4" sm="4" class="room-list">
    <div v-for="room in rooms">
    <h3 @click="openDialog(room.id)">{{ room.creator.first_name }}</h3>
    <small>{{ room.date }}</small>
    </div>
  </mu-col>

</template>

<script>

export default {
  name: 'Room',
  

  
  data(){
   return {
      rooms: '',
    }
  },
  
  created(){
    $.ajaxSetup({
      headers: {
        'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
      },
    });
    
    this.Loader()
  },
  
  methods: {
    Loader(){
      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/fh/chat/',
        type: 'GET',
        success: (response) => {
            this.rooms =  response.data.data
        } 
      })
    },
    openDialog(id){
     this.$emit("openDialog", id)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3{
  cursor: pointer;
}

.room-list{
  border-bottom: 1px solid #888

}
</style>