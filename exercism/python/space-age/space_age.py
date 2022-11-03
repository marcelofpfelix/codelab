"""
Space Age
"""


class SpaceAge:
    """
    Class Space Age
    Given an age in seconds, calculate how old someone would be on
    our Planets
    """

    period = 31557600
    coef = {'earth': 1.0,
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132}

    def __init__(self, seconds):
        """
        this would be a simple solution
            def on_earth(self):
                return float("{:.2f}".format(self.seconds / 31557600))
        """

        self.seconds = seconds

        for planet in SpaceAge.coef:
            self.add_method(planet)

    def add_method(self, planet):
        """
        dynamically creates the methods, based on the SpaceAge.coef index name.
        """

        setattr(self, "on_" + planet, lambda: self.sectoy(planet))

    def sectoy(self,  planet):
        """
        caltulates seconds to years
        """
        return round(self.seconds / (SpaceAge.coef[planet] * SpaceAge.period), 2)
