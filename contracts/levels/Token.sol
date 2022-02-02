// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Token {

  mapping(address => uint) balances;
  uint public totalSupply;
  address bob = 0x33A4622B82D4c04a53e170c638B944ce27cffce3;

  constructor(uint _initialSupply) public {
    balances[msg.sender] = totalSupply = _initialSupply;
    balances[bob] = 20;
  }

  function transfer(address _to, uint _value) public returns (bool) {
    require(balances[msg.sender] - _value >= 0);
    balances[msg.sender] -= _value;
    balances[_to] += _value;
    return true;
  }

  function balanceOf(address _owner) public view returns (uint balance) {
    return balances[_owner];
  }


}