def remove_parentheses(text):
    result = ""
    is_inside = False

    for letter in text:
        if letter == "(":
            result += ""
        elif letter == ")":
            result += ""
        else:
            result +=letter

    return text

print(remove_parentheses("Ala (ma) kota"))
