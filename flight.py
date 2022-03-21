#####Write the docstrings for this class after carefully analyzing the code.

##- Document the __init__() function and the properties with
# their corresponding docstrings.

class Flight:

    """A class that represents a Flight.

    Attributes:
        number (int): the flight number.
        origin (string): the point of take off of the flight.
        destination (string): the location where the flight is headed.
        num_passengers (int): The total number of passengers in the flight.
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

                Attributes:
                number (int): the flight number.
                origin (string): the point of take off of the flight.
                destination (string): the location where the flight is headed.
                num_passengers (int): The total number of passengers in the flight.
                total_weight_ (int): the total weight of the flight.
                pilot (string): the name of the pilot.
                crew (int): the total number of crew.
                """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

        @property
        def radius(self):
            """"""