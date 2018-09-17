<template>

    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <paper-table :title="table.title" :sub-title="table.subTitle" :data="table.data" :columns="table.columns">

          </paper-table>
        </div>
      </div>
    </div>

</template>
<script>
  import axios from 'axios'
  import PaperTable from 'components/UIComponents/PaperTable.vue'
  const tableColumns = ['id', 'Asker', 'Renter', 'Tokens', 'Status']
  const tableData = []

  export default {
    components: {
      PaperTable
    },
    data () {
      return {
        table: {
          title: 'Order Table',
          subTitle: 'Check and pick orders',
          columns: [...tableColumns],
          data: [...tableData]
        }
      }
    },
    created () {
     
    }
  }

</script>
<style>

</style>
