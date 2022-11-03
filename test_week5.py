""" week5 test class and methods """
import unittest
from week5 import Person, City, Furniture
from week5 import exchange_apples
from week5 import exchange_ideas
from week5 import max_elevation_city
from week5 import describe_furniture

class TestWeek5(unittest.TestCase):
    """ Unit tests for Week5 """

    def test_exchange_apples(self):
        """ verify exchange of apples """
        johanna = Person()
        johanna.apples = 1
        johanna.ideas = 1

        martin = Person()
        martin.apples = 2
        martin.ideas = 1

        self.assertEqual(exchange_apples(johanna, martin), (2,1))

    def test_exchange_ideas(self):
        """ verify exchange of ideas """
        johanna = Person()
        johanna.apples = 1
        johanna.ideas = 1

        martin = Person()
        martin.apples = 2
        martin.ideas = 1

        self.assertEqual(exchange_ideas(johanna, martin), (2,2))

    def test_max_elevation_city(self):
        """ verify max_elevation_city """

        # create a new instance of the City class and
        # define each attribute
        city1 = City()
        city1.name = "Cusco"
        city1.country = "Peru"
        city1.elevation = 3399
        city1.population = 358052

        # create a new instance of the City class and
        # define each attribute
        city2 = City()
        city2.name = "Sofia"
        city2.country = "Bulgaria"
        city2.elevation = 2290
        city2.population = 1241675

        # create a new instance of the City class and
        # define each attribute
        city3 = City()
        city3.name = "Seoul"
        city3.country = "South Korea"
        city3.elevation = 38
        city3.population = 9733509

        self.assertEqual(max_elevation_city(city1,city2,city3,100000), '"Cusco, Peru"')
        self.assertEqual(max_elevation_city(city1,city2,city3,1000000), '"Sofia, Bulgaria"')
        self.assertEqual(max_elevation_city(city1,city2,city3,10000000), '""')

    def test_describe_furniture(self):
        """ verify describe_furniture """
        table = Furniture()
        table.color = "brown"
        table.material = "wood"
        
        couch = Furniture()
        couch.color = "red"
        couch.material = "leather"

        self.assertEqual(describe_furniture(table),
                         "This piece of furniture is made of brown wood"
        )
        self.assertEqual(describe_furniture(couch),
                         "This piece of furniture is made of red leather"
        )
