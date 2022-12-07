<template>
  <h1>FORM</h1>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Name"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>
    
    <v-text-field
      v-model="address"
      :counter="15"
      :rules="addRules"
      label="Address"
      required
    ></v-text-field>

    <v-select
      v-model="select"
      :items="items"
      :rules="[v => !!v || 'Item is required']"
      label="Item"
      required
    ></v-select>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox>

   <v-btn
      color="success"
      @click="SubmitEvent"
    >
      SUBMIT 
    </v-btn>

    
  </v-form>
</template>


<script>
  export default {
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      address:'',
      addRules:[
        v => !!v || 'address is required',
        v => (v && v.length <= 15) || 'Address must be less than 15 characters',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    methods: {
      async SubmitEvent () {
        const { valid } = await this.$refs.form.validate()

        if (valid) alert('Form is submitted')
      }
    },
  }
</script>

<style>
h1 {
  text-align: center;
}
centre {
  text-align: center;
}</style>