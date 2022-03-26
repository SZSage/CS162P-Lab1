def getAndValidateInt(prompt):
    """ Allows the user to enter a value from the keyboard.
        When the value is an int, the function returns a tuple (True, value)
        When the value is NOT an int, the function returns a tuple (False, 0)
        Takes as a parameter the prompt to the user.
        """

    # local variable for the value
    value = 0
    # try to get the value and cast it as an int
    try:
        value = int(input(prompt))
        # this function must return 2 things so use a tuple
        return (True, value)
    # a ValueError exception will be thrown when the value is not an int
    # isnumeric or isdigit will fail for negative numbers so exceptions
    # are required to do this kind of validation
    except ValueError:
        print("That is not a whole number. ")
        return (False, value)


def getIntInRange(min, max, prompt=""):
    """ Allows the user to enter a value from the keyboard between min and max.
        User is forced to re-enter until a valid integer is entered.
        Takes as parameters min, max and the prompt to the user.
        A reasonable prompt will be displayed when none is provided.
        """
    # check the default parameter for the prompt
    if prompt == "":
        prompt = f"Please enter a whole number between {min} and {max}. "

    # because the function returns a tuple,
    # use an assignment statement with a tuple on the left
    # true or false will be assigne to isInt, the value entered by the user to value
    (isInt, value) = getAndValidateInt(prompt)

    # check to see that value is an int and is in rangle
    isValid = isInt and (value >= min and value <= max)

    # repeat as long as the input is invalid
    while not isValid:
        (isInt, value) = getAndValidateInt(prompt)
        isValid = isInt and (value >= min and value <= max)

    return value