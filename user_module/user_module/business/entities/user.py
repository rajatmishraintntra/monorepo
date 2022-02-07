from typing import List
from abc import ABC


class AbstractUser(ABC):
    role: object
    permissions: List[object]
