def remove_parentheses(text):
    result = ""
    is_inside = False
    is_first = False 
    
    for letter in text:
        if letter == "(":
            is_inside = True
        elif letter == ")":
            is_inside = False
            is_first = True
        elif not is_inside:
            if is_first:
                is_first = False
            else:
                result += letter

    return result


print(remove_parentheses("Ala (ma) kota"))
