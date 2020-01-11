"""
This file contains the classes handling the tests as described in the file 'run_tests'.

Each test method has the same description regarding the test as presented in 'run_tests'
"""

import unittest
import random
import string
import sys

from server.commands import Worker


def random_folder(string_length=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


class WorkerClassTestingStepOne(unittest.TestCase):
    """Handles the test for command and quit response"""

    def test_commands_response(self):
        """
        This test will check whether worker responds commands.
        """

        worker = Worker("127.0.0.1")

        output = worker.commands()

        self.assertTrue(output)

    def test_commands_quit(self):
        """
        This test will check quit response.
        """
        expected_results = ["\nLogged out"]
        results = []

        worker = Worker("127.0.0.1")

        results.append(worker.quit())

        self.assertListEqual(results, expected_results)


class WorkerClassTestingStepTwo(unittest.TestCase):
    """Handles the tests for login and listing the files"""

    def test_server_login(self):
        """
        This test will check login.
        Test1 : Wrong password
        Test2 : Wrong username
        Test3 : Proper login
        """
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        expected_results = ["\nWrong password!", "\nUsername not registered", "\nLogin completed."]
        results = []
        tests = [
            ["test", "1234"],
            ["test2", "123"],
            ["test", "123"]
        ]

        for test in tests:
            results.append(worker.login(
                test[0], test[1]))

        self.assertListEqual(results, expected_results)

    def test_server_list(self):
        """
        This test will check list command.
        Test1 : Listing without login.
        Test2 : Listing folder for user test
        """
        results = []
        expected_results = ["\nYou need to login to execute this command.", "\ntestfolder1"]
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        results.append(worker.list())
        worker.login("test", "123")
        results.append(worker.list())

        self.assertListEqual(results, expected_results)
