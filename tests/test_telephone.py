from brownie import accounts, Telephone
import pytest



def test_telephone():
    owner = accounts[0]
    print(owner)
    telephone = Telephone.deploy({"from":accounts[0]})
    tx = telephone.changeOwner(owner, {"from":owner})
    print(telephone.owner())