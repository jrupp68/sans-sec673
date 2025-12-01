import unittest
import subprocess
import random
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

    def test_bytes_and_strings(self):
        self.assertEqual(solution.bytes_to_str(b"this is bytes"), "this is bytes")
        self.assertEqual(solution.str_to_bytes("this is str"), b"this is str")
        self.assertEqual(solution.byte_length("🐉"), 4)
        self.assertEqual(solution.byte_length("z"), 1)

    def test_no_divide_by_zero(self):
        with self.assertRaises( ZeroDivisionError ):
            50 / 0

    def test_floating_point_math(self):
        self.assertEqual( round(0.1 + 0.2, 15), round(0.3, 15))

    def test_custom_add(self):
        for _ in range(20):
            rnd1 = solution.CustomInt(random.randint(1,100))
            rnd2 = solution.CustomInt(random.randint(100,300))
            #This test doesn't actually test anything
            #self.assertEqual( rnd1 + rnd2 , rnd1 + rnd2) 
            self.assertEqual( rnd1 + rnd2 , int(rnd1) + int(rnd2)) 

    def test_custom_add2(self):
        self.assertEqual(solution.CustomInt(25)+solution.CustomInt(10), solution.CustomInt(35))

        
  

