<template>
  <h1>SIGN UP</h1>
  <div class="register">
    <input type="text" v-model="name" placeholder="Enter Name" />
    <input type="text" v-model="email" placeholder="Enter Email" />
    <input type="password" v-model="password" placeholder="Enter Password" />
    <button v-on:click="signUp">Register</button>
  </div>
</template>


<script>
export default {
  name: 'SignUp',
          data()
          {
              return {
                name: '',
                password: '',
                email: ''
              }
          },
          methods:{
           signUp()
            {
              console.log("signup",this.name,this.email,this.password);
            }
          }
}
</script>
<style>
.register input {
  inline-size: 300px;
  block-size: 40px;
  padding-inline-start: 20px;
  display: block;
  margin-inline-end: auto;
  margin-inline-start: auto;
  margin-block-end: 30px;

}

.register button {
  width: 320px;
  height: 40px;
  border: 1px;
  background-color: aqua;
  cursor: pointer;
}
</style>