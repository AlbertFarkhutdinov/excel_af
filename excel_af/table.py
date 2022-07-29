"""
This module contains the description
of the class for tables in excel sheet.

"""


from typing import Optional, Union

from excel_af.helpers import get_instance
from pretty_repr import RepresentableObject
from excel_af.cell import Cell
from excel_af.column import Column
from excel_af.direction import Direction
from excel_af.row import Row


class Table(RepresentableObject):
    """
    Class for tables in excel sheet.

    Attributes
    ----------
    first_cell : Cell
        The cell in the first row and the first column
        of the table.
    direction : str or Direction
        Direction of table (horizontal or vertical).
    size_longitudinal : int
        Table size in longitudinal direction.
    size_transverse : int, optional, default : 2
        Table size in transverse direction.

    Methods
    -------
    get_address(shift_longitudinal, shift_transverse)
        Return the address of table cell that is shifted from the first one
        by specified numbers of rows and columns.
    get_first_cell_address()
        Return the address of the first table cell.

    """

    def __init__(
            self,
            first_cell: Cell,
            direction: Union[str, Direction],
            size_longitudinal: int,
            size_transverse: int = 2,
    ) -> None:
        """
        Initialization of `Table` instance.

        Parameters
        ----------
        first_cell : Cell
            The cell in the first row and the first column
            of the table.
        direction : str or Direction
            Direction of table (horizontal or vertical).
        size_longitudinal : int
            Table size in longitudinal direction.
        size_transverse : int, optional, default : 2
            Table size in transverse direction.

        """
        self.first_cell = first_cell
        self.direction = get_instance(direction, Direction)
        self.size_longitudinal = size_longitudinal
        self.size_transverse = size_transverse

    @property
    def size_longitudinal(self) -> int:
        """Table size in longitudinal direction."""
        return self.__size_longitudinal

    @size_longitudinal.setter
    def size_longitudinal(self, size_longitudinal: int) -> None:
        """Property setter for `self.size_longitudinal`."""
        if size_longitudinal >= 2:
            self.__size_longitudinal = size_longitudinal
        else:
            raise ValueError(
                'Longitudinal size must be integer value '
                'greater than or equal to 2.'
            )

    @property
    def size_transverse(self) -> int:
        """Table size in transverse direction."""
        return self.__size_transverse

    @size_transverse.setter
    def size_transverse(self, size_transverse: int) -> None:
        """Property setter for `self.size_transverse`."""
        if size_transverse >= 1:
            self.__size_transverse = size_transverse
        else:
            raise ValueError(
                'Transverse size must be integer value '
                'greater than or equal to 1.'
            )

    def get_address(
            self,
            shift_longitudinal: int,
            shift_transverse: Optional[int] = 0,
    ) -> str:
        """
        Return the address of table cell
        that is shifted from the first one
        by specified numbers of rows and columns.

        Parameters
        ----------
        shift_longitudinal : int
            Shift from the first cell of table
            in longitudinal direction.
        shift_transverse : int, optional, default : 0
            Shift from the first cell of table
            in transverse direction.
        shift_longitudinal

        Returns
        -------
        str
            The address of table cell
            that is shifted from the first one
            by specified numbers of rows and columns.

        """
        if shift_longitudinal > self.size_longitudinal:
            raise ValueError('Too large `shift_longitudinal`.')
        if shift_transverse > self.size_transverse:
            raise ValueError('Too large `shift_transverse`.')
        row_shift, column_shift = shift_longitudinal, shift_transverse
        if self.direction.direction == 'horizontal':
            row_shift, column_shift = shift_transverse, shift_longitudinal
        return Cell(
            row=Row(self.first_cell.row.number, row_shift),
            column=Column(self.first_cell.column.name, column_shift),
        ).address

    def get_first_cell_address(self) -> str:
        """Return the address of the first table cell."""
        return self.first_cell.address


if __name__ == '__main__':
    table = Table(
        first_cell=Cell(row=1, column='A'),
        direction='horizontal',
        size_longitudinal=3,
        size_transverse=2,
    )
