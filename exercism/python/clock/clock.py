"""
Clock
"""


class Clock:
    """
    a clock that handles times without dates.
    """
    def __init__(self, hour, minute):
        # add the extra hours in minutes and remove a day overflow
        # // to return an int
        self.hour = (hour + minute // 60) % 24
        print(self.hour)
        # remove an hour overflow
        self.minute = minute % 60

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return other.hour == self.hour and other.minute == self.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

print(repr(Clock(-121, -5810)))