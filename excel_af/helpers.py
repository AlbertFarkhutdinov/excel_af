"""
This module contains helper functions
that are used in `discrete_sports` package.

"""


from typing import Any


def get_instance(
        instance: Any,
        class_name: Any,
        **kwargs,
) -> Any:
    """
    Return `instance` if it is the instance of `class_name`
    or return new instance of `class_name` initialized with `instance`.

    Parameters
    ----------
    instance : any object
        An object which type is checked.
    class_name : any object
        A type of the returnable object.

    Returns
    -------
    class_name
        `instance` if it is the instance of `class_name`
        or new instance of `class_name` initialized with `instance`.

    """
    if isinstance(instance, class_name):
        return instance
    return class_name(instance, **kwargs)


def math_round(
        number: float,
        number_of_digits_after_separator: int = 0,
) -> float:
    """
    Return rounded float number.

    Parameters
    ----------
    number : float
        Number to be rounded.
    number_of_digits_after_separator
        Number of digits after
        decimal separator in `number`.

    Returns
    -------
    float
        Rounded float number.

    """
    _multiplier = int('1' + '0' * number_of_digits_after_separator)
    _number_without_separator = number * _multiplier
    _integer_part = int(_number_without_separator)
    _first_discarded_digit = int(
        (_number_without_separator - _integer_part) * 10
    )
    if _first_discarded_digit >= 5:
        _integer_part += 1
    result = _integer_part / _multiplier
    return result
