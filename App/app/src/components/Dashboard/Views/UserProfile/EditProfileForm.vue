<template>
  <div class="card">
    <div class="header">
      <h4 class="title">Place an Order</h4>
    </div>
    <div class="content">
      
     

      <div class="row">
        <form>
          <div class="col-md-4">
            <fg-input type="file"
                      placeholder="" v-on:change="handleFileUpload()">
            </fg-input>
          </div>
          <div class="col-md-4">
             <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="upload">
            Upload
          </button>
          </div>
          <div class="col-md-4" >
            <p>Order id : {{order.id}}</p>
          </div>
        </form>
        </div>
       
      
        <form>
        <div class="row">
          <div class="col-md-4">
            <fg-input type="number"
                      label="Tokens"
                      placeholder="100FOG"
                      v-model="order.tokens">
            </fg-input>
          </div>
          
          <div class="col-md-8">
            <fg-input type="text"
                      label="Private key"
                      placeholder=""
                      v-model="order.pk">
            </fg-input>
          </div>
        </div>

        
        <div class="">
          <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="updateProfile">
            Place Order
          </button>
        </div>
        <div class="clearfix"></div>
      </form>
    </div>
  </div>
</template>
<script>
// import axios from 'axios'
export default {
  data () {
    return {
      order: {
        id: '',
        file: '',
        tokens: '',
        pk: ''
      }
    }
  },
  methods: {
    updateProfile () {
   
    },
    upload () {
    
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    }
  }
}

</script>
<style>

</style>
