"""
This module contains helper functions
that are used in `discrete_sports` package.

"""


from typing import Any, Optional, Set


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


def get_representation(
        instance: Any,
        excluded: Optional[Set[str]] = None,
        is_base_included: bool = True,
) -> str:
    """
    Return the 'official' string representation of `instance`.

    Parameters
    ----------
    instance : Any
        The instance, which representation is returned.
    excluded : set, optional
        Names of arguments that are excluded
        from the representation.
    is_base_included : bool, optional, default: True
        If it is True, arguments of base class are included.

    Returns
    -------
    str
        The 'official' string representation of `instance`.

    """
    _class_name = instance.__class__.__name__
    representation = [
        f'{_class_name}(',
    ]
    for _key, _value in instance.__dict__.items():
        _key_repr, _value_repr = _key, _value
        if is_base_included:
            _parent_class = instance.__class__.__bases__[0]
            while _parent_class.__name__ != 'object':
                if _key.startswith(f'_{_parent_class.__name__}__'):
                    _key_repr = _key[3 + len(_parent_class.__name__):]
                    break
                _parent_class = _parent_class.__bases__[0]
        if _key.startswith(f'_{_class_name}__'):
            _key_repr = _key[3 + len(_class_name):]
        if excluded and _key_repr in excluded:
            continue
        if isinstance(_value, (tuple, list)):
            _value_repr = tuple(_value)
        representation.append(f'{_key_repr}={_value_repr!r}')
        representation.append(', ')
    if len(representation) > 1:
        representation.pop()
    representation.append(')')

    return ''.join(representation)
