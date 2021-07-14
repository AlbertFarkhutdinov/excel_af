"""
This module contains the description
of the class for custom excel sheet.

"""

import os
from typing import Any, Dict, List, Optional, Set, Union

import xlwings as xw

from core.helpers import math_round
from core.representable_object import RepresentableObject
from core.cell import Cell
from core.cell_checker import CellChecker
from core.column import Column
from core.row import Row
from core.table import Table


class CustomSheet(RepresentableObject):
    """
    Class for custom excel sheet.

    Attributes
    ----------
    workbook_path : str
        Path to the excel workbook.
    sheet: xlwings.Sheet
        Active sheet of the excel workbook.

    Methods
    -------
    get_boolean_value(address)
        Return boolean value from the cell with specified address.
    get_number(address, number_type, cell_checker_kwargs)
        Return the number from the cell with specified address.
    get_numbers_list(table, number_type, cell_checker_kwargs)
        Return the list of numbers number from the specified table.
    set_value(value, address, accuracy)
        Set value for the cell with specified address.
    set_numbers_list(table, values, accuracy)
        Set values for the specified table.
    clear_or_fill_table(table, accuracy, data)
        Clear specified table or fill it with the specified data.

    """

    def __init__(
            self,
            workbook_path: str,
            sheet_name: Optional[str] = None,
    ) -> None:
        """
        Initialization of `CustomSheet` instance.

        Parameters
        ----------
        workbook_path : str
            Path to excel workbook.
        sheet_name: str, optional
            Name of sheet in workbook. If it is None, active sheet is used.

        """
        self.workbook_path = workbook_path
        workbook = xw.Book(self.workbook_path)
        if sheet_name:
            self.sheet = workbook.sheets[sheet_name]
        else:
            self.sheet = workbook.sheets.active

    @property
    def excluded_attributes_for_repr(self) -> Set[str]:
        return {'sheet'}

    def get_boolean_value(
            self,
            address: str,
    ) -> bool:
        """Return boolean value from the cell with specified address."""
        return bool(self.sheet.range(address).value)

    def get_number(
            self,
            address: str,
            number_type: str,
            cell_checker_kwargs: Optional[Dict[str, Any]] = None,
    ) -> Optional[Union[float, int]]:
        """
        Return the number from the cell with specified address.

        Parameters
        ----------
        address : str
            The cell address.
        number_type : {'float', 'int'}
            Type of number in the cell.
        cell_checker_kwargs : dict, optional
            Keyword arguments for `CellChecker` instance.

        Returns
        -------
        float or int
            The number from the cell with specified address.

        """
        number = self.sheet.range(address).value
        __cell_checker_kwargs = (
            cell_checker_kwargs
            if cell_checker_kwargs is not None
            else {}
        )
        if CellChecker(
                value=number,
                address=address,
                **__cell_checker_kwargs,
        ).check():
            if number is None:
                return number
            if number_type == 'float':
                return float(number)
            if number_type == 'int':
                return int(number)
            raise ValueError('Unacceptable `number_type`.')
        return None

    def get_numbers_list(
            self,
            table: Table,
            number_type: str,
            cell_checker_kwargs: Optional[Dict[str, Any]] = None,
    ) -> List[Union[float, int]]:
        """
        Return the list of numbers number from
        the specified table.

        Parameters
        ----------
        table : Table
            The table with numbers.
        number_type : {'float', 'int'}
            Type of numbers in the table.
        cell_checker_kwargs
            Keyword arguments for `CellChecker` instance.

        Returns
        -------
        list
            The list of numbers number from
            the specified table.

        """
        numbers_list = []
        for shift_longitudinal in range(table.size_longitudinal):
            float_value = self.get_number(
                address=table.get_address(
                    shift_longitudinal=shift_longitudinal,
                ),
                number_type=number_type,
                cell_checker_kwargs=cell_checker_kwargs,
            )
            numbers_list.append(float_value)
        return numbers_list

    def set_value(
            self,
            value: Optional[Union[str, float, int]],
            address: str,
            accuracy: int,
    ) -> None:
        """
        Set value for the cell with specified address.

        Parameters
        ----------
        value : str or float or int, optional
            The value to be set.
        address : str
            The cell address.
        accuracy : int
            Required number of digits after
            decimal separator in `value`,
            if it is float.

        """
        self.sheet.range(address).value = (
            math_round(number=value, number_of_digits_after_separator=accuracy)
            if isinstance(value, float)
            else value
        )

    def set_numbers_list(
            self,
            table: Table,
            values: List[Union[str, int, float]],
            accuracy: int,
    ) -> str:
        """
        Set values for the specified table.

        Parameters
        ----------
        table : Table
            The table to be filled with numbers.
        values : str or float or int, optional
            The values to be set.
        accuracy : int
            Required number of digits after
            decimal separator in `values`,
            if they are float.

        Returns
        -------
        str
            The address of the last table cell.

        """
        address = table.get_first_cell_address()
        for shift_longitudinal in range(table.size_longitudinal):
            address = table.get_address(
                shift_longitudinal=shift_longitudinal,
            )
            self.set_value(
                value=values[shift_longitudinal],
                address=address,
                accuracy=accuracy,
            )
        return address

    def clear_or_fill_table(
            self,
            table: Table,
            accuracy: int = 2,
            data: Optional[Dict[str, Union[int, float]]] = None,
    ) -> str:
        """
        Clear specified table or fill it with the specified data.

        Parameters
        ----------
        table : Table
            The table to be filled or cleaned.
        accuracy : int, optional, default: 2
            Required number of digits after
            decimal separator in `value`,
            if it is float.
        data : dict, optional
            The data to be set in table cells.

        Returns
        -------
        str
            The address of the last table cell.

        """
        address = table.get_first_cell_address()
        for shift_longitudinal in range(table.size_longitudinal):
            for shift_transverse in range(table.size_transverse):
                try:
                    _data_list = list(data.items())
                    value = _data_list[shift_longitudinal][shift_transverse]
                except (AttributeError, IndexError):
                    value = None
                address = table.get_address(
                    shift_longitudinal=shift_longitudinal,
                    shift_transverse=shift_transverse,
                )
                self.set_value(
                    value=value,
                    address=address,
                    accuracy=accuracy,
                )
        return address


@xw.func
def main():
    """Test procedure."""
    workbook_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_sheet.xlsm'
    )
    xw.Book(workbook_path).set_mock_caller()
    sheet = CustomSheet(
        workbook_path=workbook_path,
    )
    print(sheet)
    for address in ('A1', 'B1', 'C1', 'D1', 'E1',):
        print(
            sheet.get_number(address=address, number_type='int'),
            sheet.get_boolean_value(address),
        )
    numbers_list = sheet.get_numbers_list(
        table=Table(
            first_cell=Cell(row=Row(1), column=Column('D')),
            direction='horizontal',
            size_longitudinal=4,
        ),
        number_type='int',
    )
    print(numbers_list)
    numbers_list = sheet.get_numbers_list(
        table=Table(
            first_cell=Cell(row=Row(1), column=Column('J')),
            direction='vertical',
            size_longitudinal=4,
        ),
        number_type='int',
    )
    print(numbers_list)
    sheet.set_value(value=1.156, address='B1', accuracy=2,)
    sheet.set_numbers_list(
        table=Table(
            first_cell=Cell(row=Row(1), column=Column('N')),
            direction='vertical',
            size_longitudinal=4,
        ),
        values=[1, 2, 3, 4, 5, 6, 7],
        accuracy=2,
    )
    table = Table(
        first_cell=Cell(row=Row(11), column=Column('A')),
        direction='vertical',
        size_longitudinal=6,
        size_transverse=2,
    )
    sheet.clear_or_fill_table(
        table=table,
        accuracy=2,
    )
    sheet.clear_or_fill_table(
        table=table,
        data={
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        },
        accuracy=2,
    )


if __name__ == "__main__":
    print(repr(CustomSheet('test_sheet.xlsm')))
    # main()
