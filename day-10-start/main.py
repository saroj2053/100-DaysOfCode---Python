# Functions With Outputs

def format_name():
    f_name = input("Enter your first name\n")
    l_name = input("Enter your lastname\n")
    full_name = f_name + " " + l_name
    return full_name


result = format_name()
result = result.title()
print(result)


# Functions Having more than one return statements
def format_username(firstname, lastname):
    # Docstrings
    """Take a first and last name and format it
     to return the title case version of the name."""
    if firstname == "" or lastname == "":
        return "You didn't provide valid inputs."
    formatted_f_name = firstname.title()
    formatted_l_name = lastname.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_username(input("What is your first name? "), input("What is your last name? ")))

