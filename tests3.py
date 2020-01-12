"""
Tests
"""

def is_finished_with_step(test_case_class_to_use):
    """Helper function to initialize, load, and run tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(
        loader.loadTestsFromTestCase(
            test_case_class_to_use
        )
    )

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.skipped:
        return False

    return result.wasSuccessful()


def is_finished_with_step_one():
    """Run the first batch of tests"""
    print('-'*70 + "\nStarting test suite 1:\n")
    return is_finished_with_step(WorkerClassTestingStepOne)

def is_finished_with_step_two():
    """Run the second batch of tests"""
    print('-'*70 + "\nStarting test suite 2:\n")
    return is_finished_with_step(WorkerClassTestingStepTwo)

def is_finished_with_step_three():
    """Run the second batch of tests"""
    print('-'*70 + "\nStarting test suite 3:\n")
    return is_finished_with_step(WorkerClassTestingStepThree)

def is_finished_with_step_four():
    """Run the second batch of tests"""
    print('-'*70 + "\nStarting test suite 4:\n")
    return is_finished_with_step(WorkerClassTestingStepFour)

if __name__ == "__main__":
    if is_finished_with_step_one() is not True:
        print("\n\tThe first testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    elif is_finished_with_step_two() is not True:
        print("\n\tThe second testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    elif is_finished_with_step_three() is not True:
        print("\n\tThe third testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    elif is_finished_with_step_four() is not True:
        print("\n\tThe fourth testing step did not pass," +
              "either because of a failed or a skipped test.")
        print("\tFurther testing will not continue until these tests pass.")
        sys.exit(1)

    sys.exit(0)
