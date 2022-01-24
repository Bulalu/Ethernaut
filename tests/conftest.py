from brownie import accounts, web3, Wei, chain
from brownie import Contract
import pytest



@pytest.fixture(scope="module", autouse=True)
def fallback(Fallback):
    owner = accounts[0]
    fallback = Fallback.deploy({"from":owner})
    return fallback