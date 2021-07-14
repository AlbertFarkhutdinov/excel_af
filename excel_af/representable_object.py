"""This module contains description of the class with custom `repr` method."""


from typing import Set

from excel_af.helpers import get_representation


class RepresentableObject:
    """
    Class with custom representation.

    """

    def __repr__(self) -> str:
        """Return the 'official' string representation of instance."""
        return get_representation(
            self,
            is_base_included=True,
            excluded=self.excluded_attributes_for_repr
        )

    def __str__(self) -> str:
        """Return the nicely printable string representation of instance."""
        return repr(self)

    @property
    def excluded_attributes_for_repr(self) -> Set[str]:
        """Return attributes that are not shown in instance representation."""
        return set()
