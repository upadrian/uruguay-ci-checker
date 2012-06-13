def get_vdigit(ci):
    sci = str(ci).strip()
    vdigit = -1
    if (len(sci) == 7):
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
    sci = str(ci).strip()
    isValid = False;
    if (len(sci) == 8):
        vdigit = sci[7:8]
        rest = sci[:7]
        if (get_vdigit(rest) == vdigit):
            isValid = True
    return isValid

if __name__ == "__main__":
    # TEST
    print "4369706 -> " + get_vdigit(4369706)
    print "2629255 -> " + get_vdigit(2629255)
    print "IS VALID 26292556 -> " + str(validate_ci(26292556))