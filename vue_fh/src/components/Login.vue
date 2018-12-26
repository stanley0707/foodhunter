<template>
  <div>
   <mu-container class="first-login-form">
    
    <mu-form ref="form" :model="validateForm"  class="mu-demo-form">
      войти
    <mu-form-item label="email" help-text="help text" prop="email" :rules="usernameRules">
      <mu-text-field type="email" v-model="validateForm.email" prop="email"></mu-text-field>
    </mu-form-item>
    <mu-form-item label="password" prop="password" :rules="passwordRules">
        <mu-text-field type="password" v-model="validateForm.password" prop="password"></mu-text-field>
    </mu-form-item>
    <mu-form-item>
      <mu-button color="primary" @click="selflogin">войти</mu-button>
      <mu-button @click="clear">сбросить</mu-button>
    </mu-form-item>
    </mu-form>
    </mu-container>
    
    <mu-container class="registration-form">
    
    <mu-form ref="form" :model="validateRegForm" class="mu-demo-form">
      регистрация 
    <mu-form-item label="имя" prop="firstname" help-text="help text">
      <mu-text-field type="username" v-model="validateRegForm.firstname" prop="firstname"></mu-text-field>
    </mu-form-item>
   <mu-form-item label="фамилия" prop="lastname" help-text="help text">
      <mu-text-field type="username" v-model="validateRegForm.lastname" prop="lastname"></mu-text-field>
    </mu-form-item>
    <mu-form-item label="email" prop="email" help-text="help text">
      <mu-text-field type="email" v-model="validateRegForm.email" prop="email"></mu-text-field>
    </mu-form-item>
    <mu-form-item label="пароль" prop="password_reg">
        <mu-text-field type="password" v-model="validateRegForm.password_reg" prop="password_reg"></mu-text-field>
    </mu-form-item>
    <mu-form-item label="повторите пароль" prop="password_reg2" :rules="passwordRules">
        <mu-text-field type="password" v-model="validateRegForm.password_reg2" prop="password_reg2"></mu-text-field>
    </mu-form-item>
      <mu-form-item prop="is_ckook">
      <mu-checkbox label="повар" v-model="validateRegForm.is_ckook" prop="is_ckook"></mu-checkbox>
    </mu-form-item>
    <mu-form-item>
      <mu-button color="primary" @click="regUser">продолжить</mu-button>
      <mu-button @click="clear">сбросить</mu-button>
    </mu-form-item>
    </mu-form>
  
  </mu-container>

 <mu-container>
  <mu-snackbar :position="normal.position" :open.sync="normal.open">
    {{normal.message}}
    <mu-button flat slot="action" color="secondary" @click="normal.open=false">Close</mu-button>
  </mu-snackbar>
 </mu-container>
 </div> 
</template>

<script>

export default {
  name: 'Login',
  
  data () {
    return {
      positions:['bottom-start'],
      
      normal: {
        position: 'bottom',
        message: '',
        open: false,
        timeout: 8000
      },

      pattern: new RegExp(/[0-9A-Za-z]/),
      location: window.location.href,
      
      api_activate_link: 'http://127.0.0.1:8000/api/v1/fh/account/email/confirm/',
      
      usernameRules: [
        { validate: (val) => !!val, message: 'email обязатетелн'},
        { validate: (val) => val.length >= 3, message: 'это не похоже на email'}
      ],
      
      passwordRules: [
        { validate: (val) => !!val, message: 'без пароля никуда'},
        { validate: (val) => val.length >= 3 && val.length <= 15, message: 'слишком короткий пароль'},
        //{ validate: (val) => val != self.validateRegForm.password_reg, message: 'пароли не совпадают'},
        //console.log(self.validateRegForm.password_reg)
      ],
      
     validateForm: {
        email: '',
        password: '',
      },
      validateRegForm: {
        is_ckook: false,
        email: '',
        firstname: '',
        lastname: '',
        password_reg: '',
        password_reg2: '',
      },
      
      out: {},   
  
    }
  },
  
  created(){
    var key = this.location.substr(this.location.lastIndexOf('/') + 1)
    var valid_key = key.match(this.pattern)
    if (valid_key){
        this.email_activate(key)
    }
  },

  
  methods:{
     email_activate: function(key){
      $.ajax({
          url: this.api_activate_link + key + '/',
          type: "GET",

      success:(responce) => {
        var message = 'аккаунт успешно подтвержде, вы привязали' + this.validateForm.email
        this.openNormalSnackbar(message)
      },
      
      error:(responce) => {
        console.log(this.api_activate_link + key + '/')
      }
     })
    },
    
    selflogin(){
       $.ajax({
          
          url:'http://127.0.0.1:8000/auth/token/create/',
          type: "POST",
          
          data: {
            email: this.validateForm.email,
            password: this.validateForm.password,
          },

          
          success:(responce) => {
            sessionStorage.setItem('auth_token', responce.data.attributes.auth_token)
            this.$router.push({name: "home"})
          },

          error:(responce) => {
            if (responce.status === 400){
              alert('логин: ' + this.validateForm.email +' или пароль: ' + this.validateForm.password + ' неверны')
            }
          }
        });
    },
    
    clear(){
      this.$refs.form.clear()
      this.validateRegForm = {
        email: '',
        firstname: '',
        lastname: '',
        password_reg: '',
        password_reg2: '',
        is_ckook: false
      };
    
    },


    regUser() {
      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/fh/created/',
        type: 'POST',
        
        data: {
          ckook: this.validateRegForm.is_ckook,
          first_name: this.validateRegForm.firstname,
          last_name: this.validateRegForm.lastname,
          email: this.validateRegForm.email,
          password: this.validateRegForm.password_reg,
        },
        
        success: (response) => {
          var message = 'для активации мы отправили письмо на почту' + this.validateRegForm.email
          this.openNormalSnackbar(message)
          this.clear()
        },

        error: (response) => {
          var message = 'что-то пошло не так, проверьте правильность почты или повторите попытку позже'
          this.openNormalSnackbar(message)
        }
      })
    
    },

    openNormalSnackbar(message) {
      if (this.normal.timer) clearTimeout(this.normal.timer);
      this.normal.message = message
      this.normal.open = true;
      this.normal.timer = setTimeout(() => {
        this.normal.open = false;
      }, this.normal.timeout);
     }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mu-demo-form {
  width: 100%;
  max-width: 460px;
}

.first-login-form, .registration-form{
  background:#fff!important;
  border-radius: 2px;
  width: 330px;
  padding: 20px;
  margin-bottom: 10px;
  margin-right: 2%; 
}

.demo-snackbar-radio {
  margin: 8px 0;
}
</style>
