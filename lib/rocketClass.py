class Rocket:
    """
    This class allows the user to easily calculate the distance a rocket has traveled
    given velocity values -1 to 1 on an x, y, and z plane.
    """
    def __init__(self, hz = 1):
        self._current_location = [0,0,0] # x, y, z
        self._hertz = hz
        self._time_rate = 1/self._hertz
        self._previous_locations = [] # List of lists of previous velocities

    def calculatePosition(self, velocity):
        """
        This function calculate the new position of the rocket given the velocity of
        the x, y, and z directions.
        param velocity: list of three float (also works with a string) values -1 --> 1 
        return: copy of current location (old method somehow gave mem addr)
        """
        if type(velocity) != list:
            raise TypeError
        for i in range(len(velocity)):
            try:
                velocity[i] = float(velocity[i])
            except ValueError:
                raise ValueError("Value must be a float from -1 to 1")
            if velocity[i] > 1 or velocity[i] < -1:
                raise ValueError("Value must be a float from -1 to 1")
        for i in range(3):
            self._current_location[i] += velocity[i] * self._time_rate
        self._previous_locations.append(list(self._current_location))
        return list(self._current_location)

    def setHertz(self, hz: int):
        """
        This is for setting the frequency of the data input.
        param hz: int that represents the amount of data per second. Default of 1.
        """
        self._hertz = hz
        self._time_rate = 1/self._hertz

    def getPosition(self):
        """
        return: Current coordinates of the rocket in 3D space.
        """
        return self._current_location

    @staticmethod
    def getStandAloneXYZ(data: list):
        indepedants = [[],[],[]]
        for location in data:
            for i in [0,1,2]:
                indepedants[i].append(location[i])
        return indepedants
