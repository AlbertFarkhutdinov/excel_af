"""This module contains class for Excel sheet cells checker."""


from typing import Optional, Union

from pretty_repr import RepresentableObject


class CellChecker(RepresentableObject):
    """
    Class for Excel sheet cells checker.

    Attributes
    ----------
    value : str or float or int, optional
        Value in the cell that is checked.
    address : str
        The cell address.
    condition : callable
        The condition which the cell value must satisfy.
    error_message : str, optional, default: ''
        The last part of the message about error that is raised
        if the cell value is not satisfied condition.
        It contains recommendations about required values.

    Methods
    -------
    get_error_message_for_cell()
        Return the first part of the message about error that is raised
        if the cell value is not satisfied condition.
        It contains address of the cell with unacceptable value.
    check()
        Check the cell for the condition
        and return True if the condition is satisfied.

    """

    def __init__(
            self,
            value: Optional[Union[str, float, int]],
            address: str,
            condition: callable = lambda x: True,
            error_message: str = '',
    ):
        """
        Initialization of `CellChecker` instance.

        Parameters
        ----------
        value : str or float or int, optional
            Value in the cell that is checked.
        address : str
            The cell address.
        condition : callable
            The condition which the cell value must satisfy.
        error_message : str, optional, default: ''
            The last part of the message about error that is raised
            if the cell value is not satisfied condition.
            It contains recommendations about required values.

        """
        self.value = value
        self.address = address
        self.condition = condition
        self.error_message = error_message

    def get_error_message_for_cell(self) -> str:
        """
        Return the first part of the message about error that is raised
        if the cell value is not satisfied condition.
        It contains address of the cell with unacceptable value.

        """
        return f'Unacceptable value of the cell `{self.address}`.'

    def check(self) -> bool:
        """
        Check the cell for the condition
        and return True if the condition is satisfied.

        Raises
        -------
        ValueError
            If the condition is not satisfied.

        """
        if self.condition(self.value):
            return True
        raise ValueError(
            self.get_error_message_for_cell() + '\n' + self.error_message,
        )
