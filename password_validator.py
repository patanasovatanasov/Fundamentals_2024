def validator(pwd):
    int_counter = 0
    symbol_counter = 0
    valid_pwd_sym = True
    valid_pwd_int = True
    length_validator = None
    to_list = [x for x in passwd]
    if 6 <= len(to_list) <= 10:
        length_validator = True
    else:
        length_validator = False
    for x in to_list:
        if 48 <= ord(x) <= 57:
            int_counter += 1
        elif not 65 <= ord(x) <= 90 and not 97 <= ord(x) <= 122:
            symbol_counter += 1
    if int_counter < 2:
        valid_pwd_int = False
    if symbol_counter > 0:
        valid_pwd_sym = False
    if valid_pwd_sym and valid_pwd_int and length_validator:
        return "Password is valid"
    elif not length_validator and valid_pwd_int and valid_pwd_sym:
        return "Password must be between 6 and 10 characters"
    elif not length_validator and valid_pwd_int and not valid_pwd_sym:
        return f"Password must be between 6 and 10 characters\nPassword must consist only of letters and digits"
    elif not length_validator and not valid_pwd_int and valid_pwd_sym:
        return f"Password must be between 6 and 10 characters\nPassword must have at least 2 digits"
    elif length_validator and valid_pwd_int and not valid_pwd_sym:
        return "Password must consist only of letters and digits"
    elif length_validator and not valid_pwd_int and valid_pwd_sym:
        return "Password must have at least 2 digits"
    elif length_validator and not valid_pwd_int and not valid_pwd_sym:
        return f"Password must consist only of letters and digits\nPassword must have at least 2 digits"


passwd = input()
print(validator(passwd))
