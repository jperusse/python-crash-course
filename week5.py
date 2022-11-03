# Week5
""" Week5 exercises """

class Person:
    """ A person has apples and ideas """
    apples = 0
    ideas = 0

class City:
    """ define a basic city class """
    name = ""
    country = ""
    elevation = 0 # in meters
    population = 0

class Furniture:
    """ Piece of furniture """
    color = ""
    material = ""

def exchange_apples(you:Person, me:Person):
    """
    #Here, despite G.B. Shaw's quote, our characters have started with
    #different amounts of apples so we can better observe the results.
    #We're going to have Martin and Johanna exchange ALL their apples with
    #one another.
    #Hint: how would you switch values of variables,
    #so that "you" and "me" will exchange ALL their apples with one another?
    #Do you need a temporary variable to store one of the values?
    #You may need more than one line of code to do that, which is OK.
    """
    apples = you.apples
    you.apples = me.apples
    me.apples = apples
    return you.apples, me.apples

def exchange_ideas(you:Person, me:Person):
    """
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to
    #each idea attribute? Do you need a temporary variable to store
    #the sum of ideas, or can you find another way?
    #Use as many lines of code as you need here.
    """
    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

def max_elevation_city(city1:City, city2:City, city3:City, min_population):
    """ return highest city """
	# Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()
    return_city.elevation = 0

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    #Format the return string
    if return_city.name:
        return f'"{return_city.name}, {return_city.country}"'
    else:
        return '""'

def describe_furniture(piece:Furniture):
    """ Print all attributes """
    return f"This piece of furniture is made of {piece.color} {piece.material}"
