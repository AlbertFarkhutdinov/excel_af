"""This module contains class for directions of excel tables."""


from core.representable_object import RepresentableObject


class Direction(RepresentableObject):
    """
    Class for directions of excel tables.

    Attributes
    ----------
    direction : str
        The excel table direction.

    """

    def __init__(
            self,
            direction: str,
    ) -> None:
        """
        Initialization of `Column` instance.

        Parameters
        ----------
        direction : str
            The excel table direction.

        Raises
        ------
        ValueError
            If `direction` is not in {'horizontal', 'vertical'}

        """
        self.direction = direction

    @property
    def direction(self) -> str:
        """
        Return the excel table direction.

        Raises
        ------
        ValueError
            If `direction` is not in {'horizontal', 'vertical'}.

        """
        return self.__direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """Property setter for `self.direction`."""
        if direction in {'horizontal', 'vertical'}:
            self.__direction = direction
        else:
            raise ValueError('Unacceptable direction.')

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return self.direction
