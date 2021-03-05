import unittest
import FizzBuzz

class TestFizzBuzz (unittest.TestCase):
  #
  def test_FizzBuzz(self):
    self.assertEqual(FizzBuzz.FizzBuzz(5), "Buzz")
    self.assertEqual(FizzBuzz.FizzBuzz(100), "Buzz")
    self.assertEqual(FizzBuzz.FizzBuzz(50), "Buzz")

    self.assertEqual(FizzBuzz.FizzBuzz(3), "Fizz")
    self.assertEqual(FizzBuzz.FizzBuzz(99), "Fizz")
    self.assertEqual(FizzBuzz.FizzBuzz(66), "Fizz")
    
if __name__ == '__main__':
  unittest.main()