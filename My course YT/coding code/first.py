def neew_string():
    new_string = input("")
    print(len_str := len(new_string))
    if len_str < 4 or len_str > 25:
        return False
    if new_string[0] == "_" or new_string[len_str - 1] == "_" or new_string[0].isdigit():
        return False
    for char in new_string:
        if not char.isalpha() and not char.isdigit() and char != "_":
            return False
    return True
print(neew_string())