var WBCHToken = artifacts.require("./WBCHToken");
module.exports =function(deployer) {
	deployer.deploy(WBCHToken, "0x25729b0eafb35BF850561bfFDA87C1f1A5AB2F36")
        //const WBCHToken = await WBCHToken.deployed()
  // Use deployer to state migration tasks.
};
