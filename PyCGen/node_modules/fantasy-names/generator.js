// Dependencies
var fs = require('fs'), path = require('path'), seedrandom = require('seedrandom');

module.exports = function(group, individual, quantity, type, seed) {
	if(arguments.length < 2) {
		console.error("Usage: fantasy-names GROUP INDIVIDUAL [QUANTITY=1] [TYPE=0] [SEED]");
	} else {
		if(typeof quantity === 'undefined') quantity = 1;
		if(typeof type === 'undefined') type = 0;
		if(typeof seed !== 'undefined') seedrandom(seed, {global: true});
		
		try {
			// TODO Refactor from global functions to FantasyNames.generators.group.individual
			eval(fs.readFileSync(path.join(__dirname, 'generators/'+group+'/'+individual+'.min.js'),'utf8'));
			var generator = eval('generator$'+group+'$'+individual);
			
			var output = "";
			for(var q = 0; q < quantity; q++) {
				output += generator(type);
				if(q < quantity - 1) output += '\n';
			}
			return output;
		} catch(e) {throw "Couldn't load: generator$"+group+"$"+individual;}
	}
}