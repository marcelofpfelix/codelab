"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new
    coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """
        1. Create the Alien Class
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
        2. The `hit` Method
        """
        self.health -= 1

    def is_alive(self):
        """
        3. The `is_alive` Method
        """
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        """
        The `teleport` Method
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        """
         The `collision_detection` Method
        """
        pass
        # return None


def new_aliens_collection(positions):
    """
    to call your Alien class with a list of coordinates.
    """
    return [Alien(position[0], position[1]) for position in positions]
