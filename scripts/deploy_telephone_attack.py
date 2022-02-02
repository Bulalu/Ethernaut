from brownie import accounts, TelephoneAttack, network, config
from scripts.helpful_scripts import get_account

from web3 import Web3



def deploy_telephone_attack():
    account = get_account()
    TelephoneAttack.deploy({"from":account}, publish_source=config["networks"][network.show_active()].get("verify")) 


def main():
    deploy_telephone_attack()