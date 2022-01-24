from brownie import network, accounts, config
from web3 import Web3



FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local-X"]

def get_account():

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    
    else:
        return accounts.add(config["wallets"]["from_key"])




# $ brownie networks add [environment] [id] host=[host] [KEY=VALUE, ...]
