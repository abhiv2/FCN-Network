<template>
  <div class="card">
    
    <div class="content">
      <div class="row">
        <div class="col-md-6">
          <h4>Rent your computations</h4>
          <h5>How to guide</h5>
         
              <ul>
                <li>Download renter script</li>
                <li>run  <span class =""> "npm install" </span></li>
                <li>Choose order from market</li>
                <li>run the script by giving command - "./compute.sh order-id your-private-key"</li>
              </ul>



          <a class="btn btn-info btn-fill btn-wd" href="http://127.0.0.1:8000/Scripts">
            Download script
          </a>
        
        </div>
        
      </div>
  
      <br>
      <br>
  
     
    </div>
  </div>
</template>
<script>
  import PaperNotification from 'src/components/UIComponents/NotificationPlugin/Notification.vue'
  export default {
    data () {
      return {
        type: ['', 'info', 'success', 'warning', 'danger'],
        notifications: {
          topCenter: false
        }
      }
    },
    components: {
      PaperNotification
    },
    methods: {
      notifyVue (verticalAlign, horizontalAlign) {
        var color = Math.floor((Math.random() * 4) + 1)
        this.$notifications.notify(
          {
            message: 'Welcome to <b>FOGLOG</b> - a beautiful fog computing marketplace.',
            icon: 'ti-gift',
            horizontalAlign: horizontalAlign,
            verticalAlign: verticalAlign,
            type: this.type[color]
          })
      }
    }
  }

</script>
<style>
  
</style>
