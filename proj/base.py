"""
Base Main Class
"""
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
logging.basicConfig()


class Main(object):
    """A class and some docs

    Attributes:
        - my_string (str): Some string
        - my_int (int): Some int
    """

    def __init__(self, arg1, arg2):
        """Create a Main object

        Args:
            - arg1 (str): Some string
            - arg2 (int): Some int
        """
        self.my_string = arg1
        self.my_int = arg2

    def run(self, upper=False):
        """Return a concat of attrs

        Args:
            upper (bool): If we should return uppercase strings

        Returns:
            A concatted string
        """
        if upper:
            return self.my_string.upper() + ' ' + str(self.my_int)
        else:
            return self.my_string + ' ' + str(self.my_int)
