import unittest
import LeapYear

class TestLeapYear (unittest.TestCase):
  #
  def test_LeapYear(self):
    self.assertEqual(LeapYear.LeapYear(2000), "is leap year")
    self.assertEqual(LeapYear.LeapYear(1600), "is leap year")
    self.assertEqual(LeapYear.LeapYear(1200), "is leap year")

    self.assertEqual(LeapYear.LeapYear(1700), "NOT a leap year")
    self.assertEqual(LeapYear.LeapYear(1800), "NOT a leap year")
    self.assertEqual(LeapYear.LeapYear(1900), "NOT a leap year")

    self.assertEqual(LeapYear.LeapYear(2004), "is leap year")
    self.assertEqual(LeapYear.LeapYear(2008), "is leap year")
    self.assertEqual(LeapYear.LeapYear(1996), "is leap year")

    self.assertEqual(LeapYear.LeapYear(1969), "NOT a leap year")
    self.assertEqual(LeapYear.LeapYear(1774), "NOT a leap year")
    self.assertEqual(LeapYear.LeapYear(1830), "NOT a leap year")



    
if __name__ == '__main__':
  unittest.main()