# Python ERC20
Python code and solidity smart contract to allow to easily create erc20 tokens with python.

### Useage
1. Deploy smart contract to a network of your choosing.

2. Copy the deployment address for the smart contract and paste into ERC20.py

3. Enter your rpc endpoint / provider, public and private keys and the chain id into ERC20.py

4. Call the function with the appriate arugments. There is an example call which can be uncommented and arguments changed at the end of ERC20.py.

example useage - createERC20('My Token', 'MT', 100000, True, False) will create a token called My Token with a ticker MT, a total supply of 100 000 tokens and it will be burnable but not minatable.
