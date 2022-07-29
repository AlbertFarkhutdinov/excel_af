"""This module contains class for Excel sheet cells."""


from __future__ import annotations
from typing import Optional, Tuple, Union

from pretty_repr import RepresentableObject

from excel_af.helpers import get_instance
from excel_af.column import Column
from excel_af.row import Row


class Cell(RepresentableObject):
    """
    Class for Excel sheet cells.

    Attributes
    ----------
    address : str, optional
        The cell address.
    row : Row or int, optional
        The cell row number.
    column : Column or str, optional
        The cell column name.

    """

    @staticmethod
    def get_row_and_column_from_address(address: str) -> Tuple[Row, Column]:
        """
        Return row number and column name corresponding
        to the cell in the Excel sheet with specified address.

        Parameters
        ----------
        address : str
            Address of the cell in the Excel sheet.

        Returns
        -------
        row : Row
            The cell row number.
        column : Column
            The cell column name.

        """
        row = int(''.join([i for i in address if i.isdigit()]))
        column = ''.join([i for i in address if i.isalpha()])
        return Row(row), Column(column)

    @staticmethod
    def get_address_from_row_and_column(
            row: Union[Row, int],
            column: Union[Column, str],
    ) -> str:
        """
        Return address of the cell in the Excel sheet
        with specified row and column.

        Parameters
        ----------
        row : Row or int, optional
            The cell row number.
        column : Column or str, optional
            The cell column name.

        Returns
        -------
        address : str, optional
            The cell address.

        """
        return f'{column}{row}'

    def __init__(
            self,
            address: Optional[str] = None,
            row: Optional[Union[Row, int]] = None,
            column: Optional[Union[Column, str]] = None,
    ) -> None:
        """
        Initialization of `Cell` instance.

        Parameters
        ----------
        address : str, optional
            The cell address.
        row : Row or int, optional
            The cell row number.
        column : Column or str, optional
            The cell column name.

        """
        if address and not row and not column:
            self.__row, self.__column = self.get_row_and_column_from_address(
                address=address
            )
            self.__address = address
        elif not address and row and column:
            self.__row = get_instance(row, Row)
            self.__column = get_instance(column, Column)
            self.__address = self.get_address_from_row_and_column(
                row=row,
                column=column,
            )
        else:
            raise ValueError('Conflict between `address`, `row` and `column`.')

    @property
    def address(self) -> str:
        """Return the cell address."""
        return self.__address

    @address.setter
    def address(
            self,
            address: Optional[str] = None,
    ) -> None:
        """Property setter for `self.address`"""
        self.__address = address
        self.__row, self.__column = self.get_row_and_column_from_address(
            address=address,
        )

    @property
    def row(self) -> Row:
        """Return the row number."""
        return self.__row

    @row.setter
    def row(
            self,
            row: Optional[Union[Row, int]] = None,
    ) -> None:
        """Property setter for `self.row`"""
        self.__row = get_instance(row, Row)
        self.__address = self.get_address_from_row_and_column(
            row=self.__row,
            column=self.__column,
        )

    @property
    def column(self) -> Column:
        """Return the cell column name."""
        return self.__column

    @column.setter
    def column(
            self,
            column: Optional[Union[Column, str]] = None,
    ) -> None:
        """Property setter for `self.column`"""
        self.__column = get_instance(column, Column)
        self.__address = self.get_address_from_row_and_column(
            row=self.__row,
            column=self.column,
        )

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return self.address


if __name__ == '__main__':
    help(Cell)
