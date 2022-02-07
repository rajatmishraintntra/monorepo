from typing import List
import abc


class AbstractRole(abc.ABC):
    """AI is creating summary for AbstractRole

    Args:
        abc ([type]): [description]
    """

    id: int
    role_name: str
    default_permissions: List[object]

    def __init__(
        self, role_name: str, default_permissions: List[object], _id=None
    ) -> None:
        """AI is creating summary for __init__

        Args:
            role_name (str): [description]
            default_permissions (List[object]): [description]
            _id ([type], optional): [description]. Defaults to None.
        """
        self.id = _id if _id is not None else 0
        self.role_name = role_name
        self.default_permissions = default_permissions
