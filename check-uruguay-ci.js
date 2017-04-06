/**
 * Checker for uruguayan ci
 *
 * @author upadrian@gmail.com
 *
 */
function CiCheck() {
	this.getDc     = function(ci) {
		var control = [2, 9, 8, 7, 6, 3, 4], sum = 0;
		ci          = String(ci);
		if(isNaN(ci) || ci.length < 6) {
			return false;
		}
		while(ci.length < 7) {
			ci = "0" + ci;
		}
		ci = ci.split("");
		for(var k in ci) {
			sum += ci[k] * control[k];
		}
		var rest = sum % 10;
		return (rest != 0) ? 10 - rest : rest;
	};
	this.isCorrect = function(ciDc) {
		ciDc = String(ciDc);
		if(isNaN(ciDc) || ciDc.length < 7) {
			return false;
		}
		var ci = ciDc.substr(0, ciDc.length - 1),
		    dc = ciDc.substr(ciDc.length - 1, 1);
		return dc == this.getDc(ci);
	}
}


