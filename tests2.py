class WorkerClassTestingStepThree(unittest.TestCase):
    """Handles the tests to check response for change folder and create folder"""

    def test_server_change_folder(self):
        """
        This test will check response for change folder.
        Test1 : Change folder without login.
        Test2 : Wrong directory change.
        Test3 : Proper directory change.
        """
        results = []
        expected_results = ["\nYou need to login to execute this command.", "\nWrong directory name.", "\nChanged directory to testfolder1 successfully"]
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        results.append(worker.change_folder("testfolder1"))
        worker.login("test", "123")
        results.append(worker.change_folder("testfolder2"))
        results.append(worker.change_folder("testfolder1"))

        self.assertListEqual(results, expected_results)

    def test_server_create_folder(self):
        """
        This test will check response for create folder.
        Test1 : Create already present directory.
        Test2 : Proper directory with random name.
        """
        results = []
        expected_results = ["\nDirectory Already Present", "\nSuccessfully made directory"]
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        worker.login("test", "123")
        results.append(worker.create_folder("testfolder1"))
        worker.change_folder("testfolder1")
        results.append(worker.create_folder("test" + random_folder()))

        self.assertListEqual(results, expected_results)



class WorkerClassTestingStepFour(unittest.TestCase):
    """Handles the final part of the tests inculting tests for read and write the files"""

    def test_server_read_file(self):
        """
        This test will check read file.
        Test1 : Read the non existing file.
        Test2 : Proper read file.
        """
        results = []
        expected_results = ["\nUnable to open requested file. Check again.", "\nCharacters from 0 to 100 are - \nDontChangeThisContent"]
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        worker.login("test", "123")
        worker.change_folder("testfolder1")
        results.append(worker.read_file("test_read2.txt"))
        results.append(worker.read_file("test_read.txt"))

        self.assertListEqual(results, expected_results)

    def test_server_write_file(self):
        """
        This test will check write file.
        Test1 : Write on non existing file.
        Test2 : Proper write file.
        """
        results = []
        expected_results = ["\nNo such file found\nWritten a new file\n", "\nWritten successfully"]
        worker = Worker("127.0.0.1")
        worker.login_credentials = {"test":["123", "admin"]}
        worker.login("test", "123")
        worker.change_folder("testfolder1")
        results.append(worker.write_file(random_folder() + ".txt", "content"))
        results.append(worker.write_file("test_write.txt", "content"))

        self.assertListEqual(results, expected_results)
