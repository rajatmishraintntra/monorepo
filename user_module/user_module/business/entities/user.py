from abc import ABC
from typing import List


class AbstractUser(ABC):
    role: object
    permissions: List[object]
