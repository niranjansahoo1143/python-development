from rest_framework.test import APITestCase


class TestDummy(APITestCase):
    def test_post_fail(self):
        self.assertEqual({"me": "0001"}, {"me": "0001"})
