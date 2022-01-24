from brownie import accounts, CoinFlipAttack, network, config
from scripts.helpful_scripts import get_account

from web3 import Web3

def deploy_coinflip_attack():
    print("Starting Deploying attack!! ")
    account = get_account()
    coinflip_attack = CoinFlipAttack.deploy({"from":account},publish_source=config["networks"][network.show_active()]["verify"])
    
def main():
    deploy_coinflip_attack()
