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
          
      (async function claim() {
      
        try {
          
        const { executionResult } = await contract.contractCall(CONTRACT_ADDRESS, encodedData, { gasLimit })
        executionResult.jobCreate.call(process.args[2], transact={'from' :mywallet, 'to' : contact_address, gas: config.gasLimit })

          return executionResult.signedTx
        }
        catch (exc) {
          throw 'something went wrong: ${exc}'
        }
      })();




      export async function check_tx_status() {
        const { data } = await axios.get(`${QTUM_TESTNET}/insight-api/sync`)
        
        if (data.status !== 'finished')
          throw 'cant get current blockchain height.'

        return data.blockChainHeight
      }
    },
    upload () {
      let formData = new FormData()
      formData.append('file', this.file)
      axios.get('http://127.0.0.1:8000/newfiles'
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(res => {
        this.order.id = res.data.data.split('.')[0]
         alert('upload complete, id =' + this.order.id )
      })
      .catch(() => {
        console.log('FAILURE!!')
      })     
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    }
  }
}

</script>
<style>

</style>
