"""This module contains class for row numbers of excel sheet cells."""


from core.representable_object import RepresentableObject


class Row(RepresentableObject):
    """
    Class for row numbers of excel sheet cells.

    Attributes
    ----------
    number : int
        The initial cell row number.
    shift : int, optional, default: 0
        Number of rows by which the cell is shifted
        relative to the initial cell row.

    """

    def __init__(
            self,
            number: int,
            shift: int = 0,
    ) -> None:
        """
        Initialization of `Row` instance.

        Parameters
        ----------
        number : int
            The initial cell row number.
        shift : int, optional, default: 0
            Number of rows by which the cell is shifted
            relative to the initial cell row.

        Raises
        ------
        ValueError
            If `number` is not positive integer number.
            If `shift` is not non-negative integer number.

        """
        self.shift = shift
        self.number = number

    @property
    def shift(self) -> int:
        """
        Return number of rows by which the cell is shifted
        relative to the initial cell row.

        Raises
        ------
        ValueError
            If `shift` is not non-negative integer number.

        """
        return self.__shift

    @shift.setter
    def shift(self, shift: int) -> None:
        """Property setter for `self.shift`."""
        if isinstance(shift, int) and shift >= 0:
            self.__shift = shift
        else:
            raise ValueError('Shift must be non-negative integer number.')

    @property
    def number(self) -> int:
        """
        Return the initial cell row number.

        Raises
        ------
        ValueError
            If `number` is not positive integer number.

        """
        return self.__number + self.shift

    @number.setter
    def number(self, number: int) -> None:
        """Property setter for `self.number`."""
        if isinstance(number, int) and number >= 1:
            self.__number = number
        else:
            raise ValueError('Cell row must be positive integer number.')

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return str(self.number)

    def __add__(self, other: int):
        return Row(number=self.number, shift=other)


if __name__ == '__main__':
    help(Row)
