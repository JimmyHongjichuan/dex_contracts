var ZRXToken = artifacts.require("./ZRXToken.sol");

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(ZRXToken);
};
