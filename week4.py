""" Week4 package with all sample code """

# Week 4
def format_address(address_string):
    """
        The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
    """
    # Declare variables
    house_number = ""
    street_name = ""

    # Separate the address string into parts
    address_parts = address_string.split()

    # Traverse through the address parts
    for part in address_parts:
        # Determine if the address part is the
        # house number or part of the street name
        if part.isnumeric() :
            house_number = part
        else:
            street_name += part + " "

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return f'"house number {house_number} on street named {street_name.rstrip()}"'

def highlight_word(sentence, word):
    """
    The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
    """
    new_list = []
    for w in sentence.split():
        if word in w:
            new_list.append(w.upper())
        else:
            new_list.append(w)
    new_sentence = " ".join(new_list)
    return new_sentence
