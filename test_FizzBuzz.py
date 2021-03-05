import unittest
import FizzBuzz

class TestFizzBuzz (unittest.TestCase):
  #
  def test_FizzBuzz(self):
    self.assertEqual(FizzBuzz.FizzBuzz(5), "Fizz")
    
if __name__ == '__main__':
  unittest.main()