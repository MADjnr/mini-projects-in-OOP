#####Write the docstrings for this class after carefully analyzing the code.

##- Document the __init__() function and the properties with
# their corresponding docstrings.

class Flight:
    """A Class that represents an international Flight.

    Attributes:
        number (str): the flight number represented as a string
        origin (str): a three-letter abbrevation of the country of origin. e.g. "USA"
        destination (str): a three-letter abbreviation of the destination
        num_passengers (int): an integer that represents the number of passengers that are currently registered
        total_weight_ (int): the total weight of the flight.
        pilot (string): the name of the pilot.
        crew (int): the total number of crew.

    Methods:
        total_weight(self):
            Returns the total weight of the plane.
        pilot(self):
            Returns the name of the pilot
        crew(self):
            Returns the name number of crew members
        display_flight_data(self):
            Returns the full data of the flight
    """

    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initialize an instance of Flight.
            Arguements:
                number (str): the flight number represented as a string
                origin (str): a three-letter abbrevation of the country of origin. e.g. "USA"
                destination (str): a three-letter abbreviation of the destination
                num_passengers (int): an integer that represents the number of passengers that are currently registered
                total_weight_ (float): the approxiamte weight of the flight including baggage, passengers
                                    fuel, crew, and other element.
                pilot (string): the pilot assigned to the flight.
                crew (int): the crew assigned to the flight.
                """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

    @property
    def total_weight(self):
       """ Total weight of the flight, including luggage, crew and fuel"""
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """Pilot assigned to the flight."""
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """
        """
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        """Crew assigned to the flight."""
        self._crew = new_crew

    def display_flight_data(self):
        """Print flight data in a user-friendly format"""
        print(" == Flight ==")
        print("Number:", self.number)
        print("Number of passenger:", self.num_passengers)
        print("Weight:", self.total_weight)
        print("Pilot:", self._pilot)
        print("crew:", self._crew)


help(Flight)
#my_flight = Flight()