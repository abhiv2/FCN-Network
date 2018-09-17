<template>
  <div class="card card-user">
   
    <div class="content">
     
      <p class="description text-center">
        Upload files for computation
        </p>
    <p>Instructions - </p>

    <ul>
      <li>Files must be a zip</li>
      <li>Zip must contain a file names - cmd.txt</li>
      <li>cmd.txt must contain the command to be run</li>
      <li>Your private key will only remain in browser and will never go to a network</li>

    </ul>



    </div>
    <hr>
    <div class="text-center">
      <div class="row">
        <p class="description">Placeholder data</p>
        <div v-for="(info,index) in details" :class="getClasses(index)">
          <h5>{{info.title}}
            <br>
            <small>{{info.subTitle}}</small>
          </h5>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        details: [
          {
            title: '12',
            subTitle: 'Files'
          },
          {
            title: '2GB',
            subTitle: 'Used'
          },
          {
            title: '24,6$',
            subTitle: 'Earned'
          }
        ]
      }
    },
    methods: {
      getClasses (index) {
        var remainder = index % 3
        if (remainder === 0) {
          return 'col-md-3 col-md-offset-1'
        } else if (remainder === 2) {
          return 'col-md-4'
        } else {
          return 'col-md-3'
        }
      }
    }
  }

</script>
<style>
  
</style>
