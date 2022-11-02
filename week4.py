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
    return sentence.replace(word, word.upper())

def combine_lists(list1, list2):
    """
    Generate a new list containing the elements of list2
    Followed by the elements of list1 in reverse order
    """
    new_list = list2
    # add list1 in reverse order
    for index in range(len(list1)-1,-1,-1):
        new_list.append(list1[index])
    return new_list

def squares(start, end):
    """"
    Return a list of consecutive squares for the given range start to end.
    """
    return [n*n for n in range(start, end+1)]

def car_listing(car_prices):
    """
    Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
    """
    result = ""
    for key, value in car_prices.items():
        result += f"{key} costs {value} dollars\n"
    return result

def combine_guests(guests1:dict, guests2:dict):
    """
    Combine two dictionaries withe first given preference
    """
    guests2.update(guests1)
    return guests2
