import unittest
from api import repo_count


class testApi(unittest.TestCase):

    def testValidity(self):
        self.assertEqual(repo_count(567), "Not a valid input for the user")


if __name__ == "__main__":
    print("Testing")
    unittest.main()
