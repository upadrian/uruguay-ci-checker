<?php

/**
 * Checker for uruguayan ci
 * 
 * @author upadrian@gmail.com
 *  
 */
 
/**
 * Get control digit from a ci number (7 / 6 digits)
 * 
 * @access public
 * @param integer CI number, without control digit, commas or points.
 * @return bool
 */
 
function get_dc_uruguay($ci) {
	if(!is_numeric($ci))
		return false;
	$ci = str_pad((string)$ci, 7, "0", STR_PAD_LEFT);
	$ci = str_split($ci);
	$control = array(2,9,8,7,6,3,4);
	$sum = 0;
	foreach($ci as $k => $v)
		$sum += $v * $control[$k];
	$rest = $sum % 10;
	return ($rest != 0)?10 - $rest:$rest;
}

/**
 * Checks whether a full CI(8 / 7 digits) is correct
 * 
 * @access public
 * @param integer CI number, with control digit. No commas or points.
 * @return bool
 * @uses get_dc_uruguay()
 */
 
function ci_is_correct_uruguay($cidc = "12345678") {
	return (!is_numeric($cidc) || strlen($cidc) < 7)?false:function ($cidc) {
		$ci = substr($cidc,0,strlen($cidc) - 1);
		$dc = substr($cidc,strlen($cidc) - 1,1);
		return $dc === get_dc_uruguay($ci);
	};
}

?>
