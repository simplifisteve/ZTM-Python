import unittest

# make tests EASY to read for everyone, don't focus on DRY principle
# def do_stuff(num=0):
#     try:
#         if num or num == 0:
#             return int(num) + 5
#         else:
#             return 'please enter a number'
#     except ValueError as err:
#         return err


# class TestMain(unittest.TestCase):
# def setUp(self):
#     print('Setting up variables!')

#     def test_do_stuff(self):
#         test_param = 10
#         result = do_stuff(test_param)
#         self.assertEqual(result, 15)

#     def test_do_stuff2(self):
#         test_param = 'asdfafdasf'
#         result = do_stuff(test_param)
#         # self.assertEqual(result, 15)
#         self.assertIsInstance(result, ValueError)

#     def test_do_stuff3(self):
#         test_param = None
#         result = do_stuff(test_param)
#         self.assertEqual(result, 'please enter a number')

#     def test_do_stuff4(self):
#         test_param = ''
#         result = do_stuff(test_param)
#         self.assertEqual(result, 'please enter a number')

#     def test_do_stuff5(self):
#         test_param = 0
#         result = do_stuff(test_param)
#         self.assertEqual(result, 5)

#     def tearDown(self):
#         print('Cleaning up variables and database!')


# if __name__ == '__main__':
#     unittest.main()

# Useful commands:
# python3 -m unittest
# python3 -m unittest -v (run all tests and give more info)

# # Testing Best Practices:
# Test one thing per test method. Keep tests focused on testing a specific behavior or case.

# Use descriptive test method names that indicate what is being tested. This helps with readability and maintaining tests.

# Test methods should be independent and not depend on other tests. Avoid shared state or dependencies between tests.

# Use test fixtures and setUp/tearDown methods to manage test dependencies and reduce duplication.

# Mock out dependencies like databases, network calls, etc to isolate the code under test.

# Check both positive and negative test cases - test with valid inputs but also invalid/edge case inputs.

# Watch out for and avoid external dependencies or test order dependencies.

# Check test coverage to make sure all code paths are exercised.

# Keep tests and production code separate. Test code should not be bundled with production code.

# Use assertions like assertEquals, assertTrue, etc to test expected vs actual results.

# Automate test runs as part of CI/CD pipelines to run tests on every code change.

# # Testing of run_game()
import random_game


class TestGame(unittest.TestCase):
    def test_input(self):
        result = random_game.run_game(5, 5)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = random_game.run_game(5, 0)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = random_game.run_game(5, 11)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = random_game.run_game(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
