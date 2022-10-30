""" Week4 package with all sample code """

def format_address(address_string):
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
  return '"house number {} on street named {}"'.format(house_number, street_name.rstrip())
