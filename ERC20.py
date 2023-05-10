from web3 import Web3

###########################################
erc20address = ''  #<enter deployed contract address>#
###########################################

###########################################
your_rpc = ''  #<enter rpc endpoint / provider>#
###########################################

###########################################
pub_key = ''  #<enter your public key>#
###########################################

###########################################
priv_key = ''  #<enter your private key>#
###########################################

###########################################
chain_id =   #<enter the chain id as integer>#
###########################################

web3 = Web3(Web3.HTTPProvider(your_rpc))

erc20abi = '''[
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "string",
          "name": "_name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "_symbol",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "_tokenType",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "_tokenAddress",
          "type": "address"
        }
      ],
      "name": "Created",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "name_",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "symbol_",
          "type": "string"
        },
        {
          "internalType": "bool",
          "name": "isBurnable_",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "isMintable_",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "initialSupply_",
          "type": "uint256"
        }
      ],
      "name": "create",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAll",
      "outputs": [
        {
          "components": [
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "symbol",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "tokenType",
              "type": "string"
            },
            {
              "internalType": "bool",
              "name": "isBurnable",
              "type": "bool"
            },
            {
              "internalType": "bool",
              "name": "isMintable",
              "type": "bool"
            },
            {
              "internalType": "address",
              "name": "tokenAddress",
              "type": "address"
            }
          ],
          "internalType": "struct Token[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
]'''


def createERC20(name, ticker, token_supply, burnable=False, mintable=False):
    global tx_hash
    contract = web3.eth.contract(erc20address, abi=erc20abi)
    nonce = web3.eth.getTransactionCount(pub_key)
    func = contract.functions.create(
    name,
    ticker,
    burnable,
    mintable,
    token_supply,
    )
    tx = func.buildTransaction({
    'from': pub_key,
    'nonce': nonce,
    'value': web3.toWei(0, 'ether'),
    'gas': 2500000,
    'gasPrice': web3.toWei('0.001', 'ether'),
    'chainId': chain_id,
    })
    signed_tx = web3.eth.account.signTransaction(tx, priv_key)
    emitted = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_hash = web3.toHex(emitted)
    return tx_hash

##################################################    
#createERC20('My Token', 'MT', 100000, True, False)  ##Example function call. Uncomment and change arguments to use
##################################################

