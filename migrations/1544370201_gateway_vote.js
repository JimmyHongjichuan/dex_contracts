var GatewayVote  = artifacts.require("./GatewayVote.sol");
var input = ["0x9ee4fc0c19b802e83e34696f4a5430e7e5b8f412","0x9dd4610b7ccc7d21543c7c17c32405ce82441bf5"]
module.exports =async function(deployer) {
	await deployer.deploy(GatewayVote, input)
	const gatewayVote = await GatewayVote.deployed()
	// Use deployer to state migration tasks.
	// };
	// ~        

	};
