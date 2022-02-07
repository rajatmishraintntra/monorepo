import unittest
from modules.common_utilities.di import obj_graph
from user_module.enterprise.services.user_service import UserService


class TestResponseTypes(unittest.TestCase):
    def test_list_user(self):
        service = obj_graph.provide(UserService)
        data = service.get_list()
        self.assertIsInstance(
            data,
            (
                list,
                dict,
            ),
        )

    def test_get_single_user(self):
        service = obj_graph.provide(UserService)
        data = service.get_single(pk=1)
        self.assertIsInstance(
            data,
            (
                list,
                dict,
            ),
        )


if __name__ == "__main__":
    unittest.main()
