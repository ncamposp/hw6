import unittest
import LeapYear

class TestLeapYear (unittest.TestCase):
  #
  def test_LeapYear(self):
    self.assertEqual(LeapYear.LeapYear(2000), "is leap year")
    self.assertEqual(LeapYear.LeapYear(1600), "is leap year")
    self.assertEqual(LeapYear.LeapYear(1200), "is leap year")



    
if __name__ == '__main__':
  unittest.main()