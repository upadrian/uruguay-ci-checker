/**
 * Checker for uruguayan ci
 * 
 * @author upadrian@gmail.com
 *  
 */
function ci(){
	this.getdc = function(ci) {
		var control = [2,9,8,7,6,3,4],sum = 0;
		ci = String(ci);
		if(isNaN(ci) || ci.length < 6)
			return false;
		while(ci.length < 7)
			ci = "0" + ci;
		ci = ci.split("");    
		for(k in ci)
			sum += ci[k] * control[k];    
		rest = sum % 10;
		return (rest != 0)?10-rest:rest;
	}
	this.iscorrect = function(cidc) {
		cidc = String(cidc);
		if(isNaN(cidc) || cidc.length < 7)
			return false;
		ci = cidc.substr(0,cidc.length - 1);
		dc = cidc.substr(cidc.length - 1,1);
		return dc == this.getdc(ci);
	}
}
var cicheck = new ci();
