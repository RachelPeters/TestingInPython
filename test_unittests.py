from unittest import TestCase

class TestUnitTests(TestCase):
    def setUp(self):
        print("Running the setup before the test")

    def tearDown(self):
        print("Running the operation after the test")

    def test_equal(self):
        sq = 'hello world'
        dq = "hello world"
        self.assertEqual(sq, dq)

    def test_notin(self):
        names = ["Prince", "Jackson", "West"]
        self.assertIn("Prince", names)
        # note test is case specific
        self.assertNotIn("prince", names)

        val = "Caribbean"
        self.assertIn("C", val)
        self.assertNotIn("a", val)

    def test_testTrue(self):
        nums = [1,2,3]
        names = None
        greaterZero = bool(len(nums) > 0)
        self.assertTrue(greaterZero)
        self.assertIsNotNone(nums)
        self.assertIsNone(names)

    def test_instance(self):
        nums = [1,2,3]
        names = ["Prince", "Jackson"]
        self.assertIsInstance(nums, list)
        self.assertIsInstance(nums[0], int)
        self.assertIsInstance(names[0], str)