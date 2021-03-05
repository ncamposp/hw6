import unittest
import FizzBuzz

class TestFizzBuzz (unittest.TestCase):
  #
  def test_FizzBuzz(self):
    self.assertEqual(FizzBuzz.FizzBuzz(5), "Fizz")
    self.assertEqual(FizzBuzz.FizzBuzz(100), "Fizz")
    self.assertEqual(FizzBuzz.FizzBuzz(50), "Fizz")
    
if __name__ == '__main__':
  unittest.main()