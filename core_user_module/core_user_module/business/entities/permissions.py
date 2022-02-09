# pylint: disable=too-few-public-methods
from abc import ABC
from typing import List


class AbstractPermissions(ABC):
    """AI is creating summary for AbstractPermissions

    Args:
        ABC ([type]): [description]
    """

    id: int
    permission_name: str
    permission_view: str
    permissions: List[bool]

    def __init__(
            self,
            permission_name: str,
            permission_view: str,
            permissions: List[bool],
            _id=None,
    ) -> None:
        """AI is creating summary for __init__

        Args:
            permission_name (str): [description]
            permission_view (str): [description]
            permissions (List[bool]): [description]
            _id ([type], optional): [description]. Defaults to None.
        """
        self.id = _id if _id is not None else 0
        self.permission_name = permission_name
        self.permission_view = permission_view
        self.permissions = permissions
