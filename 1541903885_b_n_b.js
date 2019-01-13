var BNB = artifacts.require("./BNB.sol");

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(BNB, 190799315000000000000000000, "BNB", 18, "BNB");
};
