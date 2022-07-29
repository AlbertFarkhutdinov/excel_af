"""This module contains class for column names of excel sheet cells."""


from pretty_repr import RepresentableObject


class Column(RepresentableObject):
    """
    Class for column names of excel sheet cells.

    Attributes
    ----------
    name : str
        The initial cell column name.
    shift : int, optional, default: 0
        Number of columns by which the cell is shifted
        relative to to the initial cell column.

    """

    def __init__(
            self,
            name: str,
            shift: int = 0,
    ) -> None:
        """
        Initialization of `Column` instance.

        Parameters
        ----------
        name : str
            The initial cell column name.
        shift : int, optional, default: 0
            Number of columns by which the cell is shifted
            relative to to the initial cell column.

        Raises
        ------
        ValueError
            If `name` is not single Latin capital letter.
            If `shift` is not non-negative integer number
            less than `26 - ord(self.name)`.

        """
        self.name = name
        self.shift = shift

    @property
    def shift(self) -> int:
        """
        Return number of columns by which the cell is shifted
        relative to to the initial cell column.

        Raises
        ------
        ValueError
            If `shift` is not non-negative integer number
            less than `26 - ord(self.name)`.

        """
        return self.__shift

    @shift.setter
    def shift(self, shift: int) -> None:
        """Property setter for `self.shift`."""
        _is_acceptable = (
                isinstance(shift, int)
                and (0 <= shift < 26 - ord(self.__name) + ord('A'))
        )
        if _is_acceptable:
            self.__shift = shift
        else:
            raise ValueError(
                'Column after shifting must be single Latin capital letter.'
            )

    @property
    def name(self) -> str:
        """
        Return the initial cell row number.

        Raises
        ------
        ValueError
            If `name` is not single Latin capital letter.

        """
        return chr(ord(self.__name) + self.shift)

    @name.setter
    def name(self, name: str) -> None:
        """Property setter for `self.name`."""
        _is_acceptable = (
                isinstance(name, str)
                and (len(name) == 1)
                and (ord('A') <= ord(name) <= ord('Z'))
        )
        if _is_acceptable:
            self.__name = name
        else:
            raise ValueError(
                'Cell column must be single Latin capital letter.'
            )

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return str(self.name)

    def __add__(self, other: int):
        return Column(name=self.name, shift=other)
