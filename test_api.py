import unittest
from unittest import mock
mockedReq = mock.Mock()
from api import repo_count


class testApi(unittest.TestCase):

    def testValidity(self):
        self.assertEqual(repo_count(567), "Not a valid input for the user")

    def testCommit(self):
        expected = {'555-Agile': 80,
            '567_HW2': 21,
            'Complexity': 45,
            'designpatternslab': 1,
            'GitHubAPI567': 10,
            'helloworld': 1,
            'ssw345-hw3': 4,
            'ssw345-hw4': 17,
            'ssw345-hw5': 4,
            'ssw345_node.js_lab': 1,
            'ssw567_hw1': 1}

    
    #Very unsure of what to do with this assignment. Little comprehension of what exactly is going on.
    @mock.patch('requests.get')
    def testCommit(self, mockedReq):
        # mockedReq.return_value = MockResponse('555-Agile': 80,
        #     '567_HW2': 21,
        #     'Complexity': 45,
        #     'designpatternslab': 1,
        #     'GitHubAPI567': 10,
        #     'helloworld': 1,
        #     'ssw345-hw3': 4,
        #     'ssw345-hw4': 17,
        #     'ssw345-hw5': 4,
        #     'ssw345_node.js_lab': 1,
        #     'ssw567_hw1': 1})
        commits = repo_count(self.u)
        self.assertEqual(len(commits, 81))
        
if __name__ == "__main__":
    print("Testing")
    unittest.main()
