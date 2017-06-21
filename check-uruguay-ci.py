def input_ci_filter(input_ci):
    sci = str(input_ci)
    sci = sci.replace(".", "")
    sci = sci.replace("-", "")
    sci = sci.strip()
    return sci

def get_vdigit(ci):
    sci = input_ci_filter(ci)
    vdigit = -1
    if (len(sci) == 6):
        sci = "0" + sci
    if (sci.isdigit() and len(sci) == 7):
        sum = 0
        control = [2, 9, 8, 7, 6, 3, 4]
        itControl = 0
        for strDigit in sci:
            sum += int(strDigit) * control[itControl]
            sum %= 10
            itControl += 1
        vdigit = str((10-sum) % 10)
    return vdigit

def validate_ci(ci): 
    sci = input_ci_filter(ci)
    isValid = False;
    if (len(sci) == 7):
        sci = "0" + sci
    if (sci.isdigit() and len(sci) == 8):
        vdigit = sci[7:8]
        rest = sci[:7]
        if (get_vdigit(rest) == vdigit):
            isValid = True
    return isValid

if __name__ == "__main__":
    # TEST FOR GET VDIGIT
    print ("TEST: __GET VDIGIT__")
    test_entries_get_vdigit = ["4369706", "629255", "2629255", "4.369.706", "2.629.255", "abcdefg", {}, object()]
    for entry in test_entries_get_vdigit:
        print (str(entry) + " -> " + str(get_vdigit(entry)))
    # TEST FOR VALIDATE CI
    print ("TEST: __VALIDATE CI__")
    test_entries_validate = ["43697069", "4369706-8", "4.369.706-8", "abcdefgh", {}, "6292550", object()]
    for entry in test_entries_validate:
        print (str(entry) + " -> " + str(validate_ci(entry)))

