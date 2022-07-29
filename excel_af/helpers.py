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
