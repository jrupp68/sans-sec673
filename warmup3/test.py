import unittest
import solution


class TestSolution(unittest.TestCase):

    def test_add(self):
        self.assertEqual(solution.add(5,10),15)
        self.assertEqual(solution.add(-5,-10),-15)
        self.assertEqual(solution.add(1,10),11)
        self.assertNotEqual(solution.add(1,10),15)

    def test_addmany(self):
        self.assertEqual(solution.addmany(5),5)
        self.assertEqual(solution.addmany(-5,-10),-15)
        self.assertEqual(solution.addmany(1,10,5,5,5,5),31)
        self.assertEqual(solution.addmany(1,1,1,1,1,1,1,1,1,1,-10),0)  
        self.assertNotEqual(solution.addmany(1,10),15)

if __name__ == "__main__":
    test_suite = unittest.defaultTestLoader.discover('.', 'test*.py')
    test_runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    result = test_runner.run(test_suite)

 