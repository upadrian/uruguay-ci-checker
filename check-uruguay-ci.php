<?php

/**
 * Checker for uruguayan ci
 * 
 * @author upadrian@gmail.com
 *  
 */


class ci {
    public static function getdc($ci) {
        if (!is_numeric($ci))
            return false;
        $ci = str_pad($ci, 7, "0", STR_PAD_LEFT);
        $ci = str_split($ci);
        $control = array(
            2,
            9,
            8,
            7,
            6,
            3,
            4);
        $sum = 0;
        foreach ($ci as $k => $v)
            $sum += $v * $control[$k];
        $rest = $sum % 10;
        return (int)(($rest != 0) ? 10 - $rest:$rest);
    }
    public static function iscorrect($cidc = "12345678") {
        return (!is_numeric($cidc) || strlen($cidc) < 6 || strlen($cidc) > 8) ? false:function ($cidc) {
            $ci = substr($cidc, 0, strlen($cidc) - 1);
            $dc = substr($cidc, strlen($cidc) - 1, 1);
            return (int)$dc === self::getdc($ci);
        }
    }
}
?>