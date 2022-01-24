from brownie import accounts, CoinFlipAttack, network, config
from scripts.helpful_scripts import get_account

from web3 import Web3

def deploy_coinflip_attack():
    print("Starting Deploying attack!! ")
    account = get_account()
    coinflip_attack = CoinFlipAttack.deploy({"from":account},publish_source=config["networks"][network.show_active()]["verify"])
    # for i in range(1,11):
    #     coinflip_attack.attack("0x96b73AB76615Fee44d31bfb9F8A55b3a60538650")
    print("I have successfully guessed correctly {}")
    contract = Web3.eth.contract(address='0x96b73AB76615Fee44d31bfb9F8A55b3a60538650')
    print(contract)
    
def main():
    deploy_coinflip_attack()
