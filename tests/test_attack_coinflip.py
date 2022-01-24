from brownie import accounts, CoinFlip, CoinFlipAttack
import pytest


@pytest.fixture(scope="module", autouse=True)
def deploy_coinflip():
    owner = accounts[0]
    coinflip = CoinFlip.deploy({"from":owner})
    return coinflip

@pytest.fixture(scope="module", autouse=True)
def deploy_attack_coinflip():
    owner = accounts[1]
    attack = CoinFlipAttack.deploy({"from":owner})
    return attack

def test_attack_coinflip(deploy_coinflip, deploy_attack_coinflip):
    coinflip = deploy_coinflip
    attack_coinflip = deploy_attack_coinflip
    
    for i in range(1,10):
        attack_coinflip.attack(coinflip)
        print(coinflip.consecutiveWins())