import unittest

import fizzbuzz.fizzbuzz as fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    #def test_this_will_break(self):
      #  self.assertEqual(fizzbuzz.fizzbuzz(self,1),"3")

    def test_one_returns_one_as_string(self):
        self.assertEqual(type(fizzbuzz.fizzbuzz(1)), str)

    def test_int_returns_int_as_string(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), "2")

    def test_three_returns_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")

    def test_div_by_three_returns_Fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(18), "Fizz")

    def test_five_returns_Buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")

    def test_div_by_five_returns_Buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(25), "Buzz")

    def test_div_by_both_returns_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")
