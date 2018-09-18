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


import {
  Qtum,
} from "qtumjs"


import abi from 'ethjs-abi'
import { networks } from 'qtumjs-wallet'


const domain = 'http://qtum:test@localhost:3889'

const qtum = new Qtum(domain)

const apiPrefix = domain + '/insight-api'
const config = {
  fee: 0.01,
  gasPrice: 50,
  gasLimit: 3000000
}

const mywallet = process.argv[2]
const contract_address = 'QecTRme3nR2CqG448vAXqf6YuWj8LW1DGb'
var abi = [
	{
		"constant": true,
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_spender",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "data",
				"type": "string"
			},
			{
				"name": "tokens",
				"type": "uint256"
			}
		],
		"name": "jobCreate",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "standard",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "index",
				"type": "uint256"
			},
			{
				"name": "result",
				"type": "string"
			}
		],
		"name": "jobClaim",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getJob",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getJobsLength",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"payable": true,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "",
				"type": "string"
			}
		],
		"name": "JobCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "_owner",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "_spender",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	}
]
const contract = qtum.contract(contract_address, abi)

try {
    const decoded = parseAbi(blockpost.abi)
    const index = getIndex(decoded, 'claim')
 
    const wallet = networks.testnet.fromWIF(wif)
    const signedTx = await wallet.generateContractSendTx(CONTRACT_ADDRESS, encodedData)
    const { txid } = await wallet.sendRawTx(signedTx)
  
    return txid
  }
  catch (exc) {
    throw `something went wrong: ${exc}`
  }

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
      tableData = []
     (async function claim() {
        try {
          
          const { executionResult } = await contract.contractCall(CONTRACT_ADDRESS, encodedData, { gasLimit })
          const len = executionResult.getJobsLength.call(transact={'from' :mywallet, 'to' : contact_address})
          for (const i = 0 ; i< len ; i++){
            let res  = executionResult.getJob.call(i, transact={'from' :mywallet, 'to' : contact_address})
            let newJob  =  {}
            newJob['asker'] = res[0]
            newJob['renter'] = res[1]
            newJob['tokens'] = res[2]
            newJob['id'] = res[3]
            newJob['asker'] = res[0]
            tableData.push(newJob)
          }
        }
        catch (exc) {
          throw 'something went wrong: ${exc}'
        }
      })();

        export async function check_tx_status() {
          const { data } = await axios.get(`${QTUM_TESTNET}/insight-api/sync`)
          
          if (data.status !== 'finished')
            throw 'cant get current blockchain height.'

          return data.signedTx
        }

    }
</script>
<style>

</style>
