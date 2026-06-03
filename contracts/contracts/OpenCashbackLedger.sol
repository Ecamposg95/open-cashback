// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract OpenCashbackLedger {
    address public owner;

    mapping(bytes32 => bool) public anchoredBatches;

    event BatchAnchored(bytes32 indexed batchHash, string metadataURI, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        emit OwnershipTransferred(address(0), msg.sender);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function anchorBatch(bytes32 batchHash, string calldata metadataURI) external onlyOwner {
        require(batchHash != bytes32(0), "Invalid batch hash");
        require(!anchoredBatches[batchHash], "Batch already anchored");
        anchoredBatches[batchHash] = true;
        emit BatchAnchored(batchHash, metadataURI, block.timestamp);
    }

    function isAnchored(bytes32 batchHash) external view returns (bool) {
        return anchoredBatches[batchHash];
    }
}
