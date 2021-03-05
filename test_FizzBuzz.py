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

    self.assertEqual(FizzBuzz.FizzBuzz(60), "FizzBuzz")
    self.assertEqual(FizzBuzz.FizzBuzz(90), "FizzBuzz")
    self.assertEqual(FizzBuzz.FizzBuzz(90), "FizzBuzz")

    self.assertEqual(FizzBuzz.FizzBuzz(7), "7")
    self.assertEqual(FizzBuzz.FizzBuzz(13), "13")
    self.assertEqual(FizzBuzz.FizzBuzz(97), "97")


    
if __name__ == '__main__':
  unittest.main()