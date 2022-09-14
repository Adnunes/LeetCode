# função que recebe um email e extrai apenas o nome antes da @
def email_name(email):
    at_sign = "@"
    email_name=''

    for i in email[:email.index(at_sign)]:
        email_name += i

    return print(email_name)


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for word in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if word != " ":
            new_string += word
            reverse_string = new_string[::-1]
        print(new_string.upper(), reverse_string.upper())


    # Compare the strings
    if new_string.upper() == reverse_string.upper():
        return True
    return False




